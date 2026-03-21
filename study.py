'''
#Discount Calculation
def calculate_discount(price, discount_percentage):
    discount = price * discount_percentage / 100
    final_price = price - discount
    return final_price;    

UserOrig = int(input(" Please enter the original price: "))
UserDis = int(input("Please enter the discount percentage: "))

discount = calculate_discount(UserOrig,UserDis)
print("Your discounted price is:" ,discount)

if discount >= 500:
     print("Premium purchase!")    
elif discount >= 100 and discount <= 500:
        print("Mid-range purchase!")
else:
        print("Budget Purchase!")

def calculate_electricity_bill(units_used):
    bill = units_used * 0.50
    return bill;

User = int(input("Please how many units of electricity used: "))

bill = calculate_electricity_bill(User)
print("Your electricity bill is:" ,bill)

if bill > 100:
    print("High Consumption!")
elif bill >= 50 and bill <=100:
    print("Moderate Consumption!")
else:
    print("Low Consumption!")  


#Day 5 - list built in functions sum average max min"
scores = [45, 78, 92, 61, 55, 88, 73]
print("Total:" ,sum(scores))
average = sum(scores) / len(scores)
print("Average:",(round(average, 2)))
print("Maximum:",max(scores))
print("Minimum:",min(scores))
print("Number of scores:",len(scores)) 

students = ["John","Amara","David","Sarah","James"]

for index, student in enumerate(students):
    print(index+1, "-" , student) '''

prices = [120, 45, 200, 89, 34, 156, 78]
def apply_discount(price,discount):
    discounted = price * discount / 100
    final_price = price - discounted
    return final_price;

for index, price in enumerate(prices):  
 Total = apply_discount(price,10)   
 print(index+1, ": original = " ,price, "discounted = " ,Total)
  
