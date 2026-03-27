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
    print(index+1, "-" , student) 
#"Day 5 - discount calculator with lists and functions"
prices = [120, 45, 200, 89, 34, 156, 78]
def apply_discount(price,discount):
    discounted = price * discount / 100
    final_price = price - discounted
    return final_price;

for index, price in enumerate(prices):  
 Total = apply_discount(price,10)   
 print(index+1, ": original = " ,price, "discounted = " ,Total)
  
#"Day 6 - temperatures list revision"
temperatures = [32, 45, 28, 67, 51, 39, 72]
print(max(temperatures))  
print(min(temperatures))
total = round (sum(temperatures) / len(temperatures), 2)
print(total)

for temp in temperatures:
 if temp >= 50:
    print(temp, "-", "Hot")
 else:
    print(temp, "-", "Cold") 
#"Day 6 - names list with in keyword and append"
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(len(names))
Name = str(input("Please enter your name: "))
if Name in names:
    print(Name,"is in the list!")
else:
    print(Name ,"is not in the list!")    
    names.append(Name)
print(names) 
'''

from itertools import count


numbers = [15, 42, 8, 93, 27, 64, 31, 55]
def classify_number(number):
    if number % (2) == 0:
       return "Even"
    else:
       return "Odd"    
even_count = 0      
odd_count = 0       

for index, number in enumerate(numbers):
    num = classify_number(number)
    print(index+1, number, "-", num)
    if num == "Even":
        even_count = even_count + 1    
    else:
        odd_count = odd_count + 1  

print("Total Even:", even_count)
print("Total Odd:", odd_count)