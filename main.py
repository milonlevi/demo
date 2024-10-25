import re

def main(input_str: str) -> str:
    
    match = re.match(r"(\d+)\s*([\+\-\*/])\s*(\d+)", input_str)
    if not match:
        raise ValueError("throws Exception")

    a, operator, b = match.groups()
    a, b = int(a), int(b)

    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("throws Exception") 

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b
    else:
        raise ValueError("throws Exception")

    return str(result)


try:
    vvod = input("Введите выражение: ")
    print(main(vvod))
except ValueError as e:
    print(e)