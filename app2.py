print("Choose your first number")
num1 = float(input())

print("Choose an operation (+, -, *, /)")
operation = input()

print("Choose your second number")
num2 = float(input())

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)