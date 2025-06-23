username = str(input("Enter your username: "))

username.find(" ")

username.isalpha()

if len(username) > 12:
    print("Please input a maximum of 12 characters")
elif not username.find(" ") == -1:
    print("Please there should be no spaces")
elif not username.isalpha():
    print("Please no digits")
else:
    print(username)
