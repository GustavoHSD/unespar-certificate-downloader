import os
import pyperclip
from pathlib import Path
import sys
import requests
from zipfile import ZipFile
from bs4 import BeautifulSoup
from rich.console import Console
from util import validate_cpf, clean_cpf
from rich.progress import track

URL = "http://certificados.unespar.edu.br/inicio/certificados_disponiveis"

console = Console()
output_dir = Path.home() / "Downloads"
zip_name = "certificados.zip"
output_path = os.path.join(output_dir, zip_name)

def download_certificates(links: list[str]):
    certificate_paths = []
    for i, link in enumerate(track(links, description="[bold] Downloading certificates [/ bold]")):
        try:
            response = requests.get(link, stream=True)
            certificate_path = os.path.join("/tmp", f"certificado_{i+1}.pdf")
            with open(certificate_path, "wb") as f:
                f.write(response.content)
            certificate_paths.append(certificate_path)
        except Exception:
            console.print(f"[magenta] Could not download certificate [/ magenta] [yellow] {link} [/ yellow]")
            continue

    return certificate_paths

def zip_certificates(paths: list[str]):
    with ZipFile(output_path, "w") as zipf:
        for path in paths:
            zipf.write(path, path.replace("/tmp/", ""))

def main(): 
    try:
        cpf = sys.argv[1]
    except:
        console.print("[red bold] CPF must be informed [/ red bold]")
        return

    if not validate_cpf(cpf):
        console.print("[red bold] Invalid CPF [/ red bold]")
        return -1

    cleaned_cpf = clean_cpf(cpf)

    response = requests.get(f"{URL}/{cleaned_cpf}")

    soup = BeautifulSoup(response.content, 'html.parser')
    certificates_urls = []

    certificate_table = soup.find(name="table", class_="table table-striped table-bordered table-hover")

    if not certificate_table:
        console.print(f"[red bold] CPF: {cpf} not found at unespar certificate system [/ red bold]")
        return

    for row in certificate_table.find_all(name="a", class_="btn btn-primary btn-sm"): 
        certificates_urls.append(row.get("href"))

    paths = download_certificates(certificates_urls) 
    zip_certificates(paths)
    pyperclip.copy(output_path)
    console.print(f"[bold] {len(paths)} certificates downloaded, you can find the files zipped at [magenta]{output_path}[/ magenta].\n Path copied to your clipboard [/ bold]")
 
if __name__ == '__main__':
    main()

