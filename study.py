# outside - define the function
def calculate_bmi(weight, height):
    total = weight / (height * height)
    return total  # what goes here?

# outside - ask user for input
weight = int(input("Please enter your weight: "))
height = int(input("Please enter your height: "))

# outside - call the function
bmi = calculate_bmi(weight, height)  # you finish this

# outside - check the result
if bmi < 18.5:
    print("Underweight")
elif bmi < 22:  # you finish this
    print("Healthy")
else:
      print("Overweight")  # you finish this    