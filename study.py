def calculate_grade(score):
    if score >= 90:
        return("A")
    elif score > 80 and score <= 89:
        return("B")
    elif score > 70 and score <= 79:
        return("C")
    elif score > 60 and score <= 69:
        return("D")
    else:
        return("Fail")

score = int(input("Please enter your score: "))
Result = calculate_grade(score)
print("Your grade is:" ,Result)
                    