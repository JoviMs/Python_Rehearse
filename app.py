#PYTHON Calculator

operator = input("Enter an operator of your choice (+,//,/,-,*): ")
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(round(number1 / number2, 3))
elif operator == "//":
    print(round(number1 // number2))
elif operator != "-" and operator == "//":
    print(round,(number1 % number2, 3))
else:
    print("Invalid operator")
