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

'''questions = ("What is the highest mountain in the world?",
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
'''


'''
#dictionary

capitals = {"Cameroon": "Yaounde",
            "Japan": "Tokyo",
            "USA": "Washington",}


#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "New York"})
#capitals.popitem()
items = capitals.items()
print(items) '''

'''
#Concession stand program

menu = {"mango":200,
        "apple":150,
        "popcorn":100,
        "fries":50,
        "pizza": 250
        }

cart = []
total = 0

print("--------------MENU------")
for key, value in menu.items():
    print(f"{key}: ${value: .2f}")
print ("------------------")


while True:
    food = input("Select an item(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total amount is ${total: .2f}")

print(cart) '''


#random guessing game

import random

lowest_num = 1
highest_num = 100
answer =  random.randint(lowest_num, highest_num)

print("----------GUESS THE ANSWER----------")
player1 = (input(f"Please guess your first number between {lowest_num} and {highest_num}: "))
player2 = (input(f"Please guess your second number between {lowest_num} and {highest_num}: "))
if player1.isdigit() and player2.isdigit():
    pass
else:
    print("Invalid input")
    print(f"Your number should be a digit from {lowest_num} to {highest_num}!")

player1 = int(input(f"Please guess your first number between {lowest_num} and {highest_num}: "))
player2 = int(input(f"Please guess your second number between {lowest_num} and {highest_num}: "))

if player1 < lowest_num and player2 < lowest_num:
    print("Too low!")
else:
    print("Too high!")

    player1 = int(input(f"Please guess your first number between {lowest_num} and {highest_num}: "))
    player2 = int(input(f"Please guess your second number between {lowest_num} and {highest_num}: "))

if player1 == answer or player2 == answer:
    print("Correct! you guess the exact number!")
else:
    print(f"Incorrect! both of your guesses was {player1} and {player2} which is not it. !")
print(answer)