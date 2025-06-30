''' username = str(input("Enter your username: "))

username.find(" ")

username.isalpha()

if len(username) > 12:
    print("Please input a maximum of 12 characters")
elif not username.find(" ") == -1:
    print("Please there should be no spaces")
elif not username.isalpha():
    print("Please no digits")
else:
    print(username) '''


# python quiz

questions = ("What is the highest mountain in the world?",
             "what is the coldest place in the world?",
             "what is the biggest land animal in the world?",
             "Most spoken language inthe world?",
             "The most populated country in the world?")

options = (("A.Kilimanjaro" " B.Everest" " C.Fako" " D.None"),
           ("A. Ndu" "B.USA" "C.Alaska" "D.Canada"),
           ("A.Elephane" " B.Whale" " C.Lion" " D.Crocodile"),
           ("A.Chinese" " B.Hindi" " C.French" " D.English"),
           ("A.US" " B.India" " C.China" " D.Russia"),
           )

answers = ("B", "C", "A", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("-----------------------------")
print("           RESULTS           ")
print("-----------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")
