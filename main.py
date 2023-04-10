n1 = float(input("What is first number, Filililipe: "))
op = input("Enter operator (+, -, /, *, %): ")
n2 = float(input("What is second number, Filipe: "))

if op == "+":
    result = n1 + n2
    print(round(result, 3))
elif op == "-":
    result = n1 - n2
    print(round(result, 3))
elif op == "/":
    result = n1 / n2
    print(round(result, 3))
elif op == "*":
    result = n1 * n2
    print(round(result, 3))
elif op == "%":
    result = n1 % n2
    print(round(result, 3))

else:
    print(f"{op} is not valid input")

