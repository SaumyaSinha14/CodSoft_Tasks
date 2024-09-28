def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Zero Division Error!"
    return n1 / n2

def floor(n1, n2):
    if n2 == 0:
        return "Zero Division Error!"
    elif isinstance(n1, complex) or isinstance(n2, complex):
        return "Floor division is not supported for complex numbers."
    return n1 // n2

def mod(n1, n2):
    if isinstance(n1, complex) or isinstance(n2, complex):
        return "Modulus is not supported for complex numbers."
    return n1 % n2

def exp(n1, n2):
    return n1 ** n2

def get(x):
    try:
        if 'j' in x:
            return complex(x)
        elif '.' in x:
            return float(x)
        else:
            return int(x)
    except ValueError:
        return "Invalid Input"

i = 1
while i != 0:
    print("******Calculator******\n")
    print("Choose the operations from below\n")
    print("1. '+' for addition\n2. '-' for subtraction\n3. '*' for multiplication\n4. '/' for division\n5. '//' for floor division\n6. '%' for modulus\n7. '**' for exponent")

    op = input("Enter the operation symbol: ")
    a = input("Enter the value of a: ")
    b = input("Enter the value of b: ")

    a = get(a)
    b = get(b)
    if isinstance(a, str) or isinstance(b, str):
        print("Invalid input! Please enter valid numbers.\n")
        continue

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    elif op == '//':
        result = floor(a, b)
    elif op == '%':
        result = mod(a, b)
    elif op == '**':
        result = exp(a, b)
    else:
        print("Invalid operation choice!\n")
        i = 0
        continue

    print(f"The result of {a} {op} {b} is: {result}\n")
