#python currency converter

currency = int(input("How much do you want to convert? : "))
convert = input("From which currency do you want to convert from USD or Euro?: ")

if convert == "Euro":
    amount = currency * 1.15
    print(f"The converted amount from Euros is {amount}usd.")
elif convert == "USD":
    amount = currency * 0.87
    print(f"The converted amount from USD is {amount}euro.")
else:
    print(f"You gave a wrong currency for your exchange!")
