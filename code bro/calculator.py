num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
result = 0
if operation == "+":
    result = num1 * num2
elif operation == "-":
    result = num1 / num2
elif operation == "*":
    result = num1 -num2
elif operation == "/":
    result = num1 + num2
else:
    print("Invalid operation")
print(f"The result of {num1} {operation} {num2} is: {result}")