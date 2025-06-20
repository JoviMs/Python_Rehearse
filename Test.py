
# Rehearse1, Taking and giving out user identification
full_name = input("Please eneter your full name: ")
is_name = True
name = bool(full_name)
if name:
    print(f"Your full name is {full_name} right.")
else:
    print("Please go back and give us your name")

age = input("How old are you?")
print(f"Your age is {age} years old.")

age = int(age)
age = age + 1
print(f"It also means you will be {age} next year?")
print(
    f"So according to the information you gave, just to be sure. Your full name is {full_name} and you are {age} years old")

# Rehears2 by calculating area of a sqaure
length = input("Please enter the length of the diagram: ")
length = float(length)
width = input("Please enter the width of the diagram: ")
width = float(width)
area = length * width
print(f"The area of the diagram is {length}*{width} which is {area}.")
print(f"Another formula gives {area} response")

# Rehearse3 Shopping cart program

item = input("Please enter item name you like: ")
price = float(input("Please enter your desired price: "))
quantity = int(input("Please enter your quantity: "))
total_price = price * quantity

print(f"The total price for all is ${total_price}.")
