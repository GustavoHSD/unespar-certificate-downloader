def validate_cpf(cpf: str) -> bool:
    cleaned_cpf = ''.join(filter(str.isdigit, cpf))

    if len(cleaned_cpf) != 11:
        print("CPF must have 11 digits")
        return False

    cpf_arr = [int(digit) for digit in cleaned_cpf]

    first_digit = cpf_arr[-2]
    second_digit = cpf_arr[-1]

    sum_val = sum(cpf_arr[i] * (10 - i) for i in range(9))
    first_digit_sum = (sum_val * 10) % 11
    if first_digit_sum == 10:
        first_digit_sum = 0
    if first_digit_sum != first_digit:
        print("Invalid CPF")
        return False

    sum_val = sum(cpf_arr[i] * (11 - i) for i in range(10))
    second_digit_sum = (sum_val * 10) % 11
    if second_digit_sum == 10:
        second_digit_sum = 0
    if second_digit_sum != second_digit:
        print("Invalid CPF")
        return False

    return True


def format_cpf(cpf: str) -> str:
    cleaned_cpf = ''.join(filter(str.isdigit, cpf))
    formatted_cpf = (
        f"{cleaned_cpf[:3]}.{cleaned_cpf[3:6]}.{cleaned_cpf[6:9]}-{cleaned_cpf[9:11]}"
    )
    return formatted_cpf

def clean_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))
