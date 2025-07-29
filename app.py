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
from selectors import SelectSelector
from sys import modules

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

'''
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
print(answer) '''

'''
#Banking app
def show_balance(balance):
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(f"Your balance is ${balance: .2f}")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")

def deposit():
    amount = float(input("How much do you want to deposit: "))
    if amount < 0:
        print("&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("You cannot deposit negative amounts, have some shame!")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("How much do you want to withdraw: "))

    if amount > balance:
        print("&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("You cannot withdraw more than your balance!")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    elif amount < 0:

        print("&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("You cannot withdraw negative amounts, what happen to your way of thinking!")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************************")
        print("        Banking Program      ")
        print("*****************************")
        print("Banking program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("******************************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("**********************")
            print("That is an invalid amount!")
            print("**********************")

    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("Thank you and have a nice day!")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")

if __name__ == '__main__':
    main()
'''
'''
import random

def spin_row():
    symbols = ['🍓', '🍌', '🍎', '🥑', '🧅']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("*************")
    print(" | " .join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] ==row[2]:
        if row[0] == '🍓':
            return bet * 3
        elif row[0] == '🍌':
            return bet * 5
        elif row[0] == '🥑':
            return bet * 6
        elif row[0] == '🧅':
            return bet * 10
    return 0

def main():
    balance = 100
    print("*********************")
    print("Welcome to game slots")
    print("Symbols: 🍓 🍌 🍎 🥑 🧅")
    print("*********************")

    while balance > 0:
        print(f"Your balance is ${balance: .2f}")

        bet = input("How much do you want to bet: ")
        if not bet.isdigit():
            print("Please enter a number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance!")
            continue
        if bet <= 0:
            print("Please enter a positive number.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout: .2f}")
        else:
            print("Sorry, you didn't win anything.")

        balance += payout

        play_again = input("Would you like to play again? (y/n): ")
        if play_again == "y":
            break
        print("********************************")
        print(f"Your balance is ${balance: .2f}")
        print("********************************")


if __name__ == "__main__":
    main()   
'''

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print (f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#decrypt
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    cipher_text += key[index]
print (f"original message: {cipher_text}")
print(f"encrypted message: {plain_text}")