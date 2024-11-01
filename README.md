# Unespar Certificate Donwload CLI
Simple cli-app that donwloads all certificates emitted by unespar to a specified cpf

## Installation
To install locally I recommend creating a python virtual environment with venv and install all the dependencies from the requirements.txt
```
pip install -r requirements.txt
```

## Usage
The only argument is the cpf, if the cpf is registered in the UNESPAR system it will donwload it and a file named `certificate.zip` should appear in your Donwloads folder

### Exemple
```
python3 main.py 111.222.333-99
```
If the cpf exists the output should be something like:

```
 Downloading certificates  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:54
 28 certificates downloaded, you can find the files zipped at /home/ghd8/Downloads/certificados.zip.
 Path copied to your clipboard
```
