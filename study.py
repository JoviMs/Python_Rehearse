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

#"Day  - classify numbers with even odd counter"
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


#Dictionaries
person = {
    "name": "Jovi",
    "age": 25,
    "city": "Deggendorf"
}

print(person["age"])
print(person["city"])
print(person["name"])
person["language"] = "French"
for key in person.keys():
    print(key) 

phone_book = {
    "Amanda" : 2371234567,
    "Brandon" : 3210987565,
    "Carl" : 6752982013
}
for person in phone_book.values():
    print(person)
print("Alice" in phone_book)
del phone_book["Amanda"] 

grades = {
    "mathematics": 90,
    "Physics": 70,
    "Chemistry": 68,
    "Computer": 80
}
for key, value in grades.items():
    print(key, value)
grades["Further maths"] = 95
grades["Computer"] = 85
print(grades)

def long_words(words):
    for word in words:
        if len(word) > 4:
            print(word) 
#list even numbers            
def list_numbers(numbers):    
    result = []               
    for number in numbers:
        if number % 2 == 0 :   
            result.append(number) 
    return result 

students = {
    "Junior": 85, "Bob": 40, "Alice": 72, "Tom": 30, "Niba":20, "Kimbo":49, "Jovi":90
    }
for key,value in students.items():
    if value > 50:
        print(key)               
#as a function
def list_students(students):
    result = []
    for key, value in students.items():
        if value > 50:
            result.append(key)
    return result         

def names_students(names):
    result = {}               
    for key, value in names.items():
        result[key] = value + 10
    return result 




def list_word(wordss):
    for word in words:
        if number % 2 == 0:
            result.append(number)
    Average = sum(numbers) / len(numbers)            
    return Average'''

'''
#explaining threads changing to process, about heaps
from threading import Thread
from multiprocessing import Process, Queue
import time, random
num_threads = 2
my_thread = []
my_common_list = []
q = Queue

def my_calc(x):
    sum = 0
    for i in range(x)
    sum = sum + 1

def add_list_item(x, q):
    for i in range(10):
        #my_common_list.append(str(x)+"-"+str(i))
        q.put([x,i])
        time.sleep(random.randint(1,5) * 0.1)

def get_q_items(x,q):
    while True:
        msg = q.get()
        print(msg)

start = time.time()

for i in range(num_threads):
    #my_thread.append(Thread(target=my_calc, args(10000000)))
    my_thread.append(Process(target=my_calc, args(i, q))) '''


# create two agents that cann communicate through a queue (EXAMS VIBE)
import queue
import threading
import time


def agent1(q):
    for i in range(5):
        q.put(f"Message {i} from Agent 1")
        time.sleep(1)


def agent2(q):
    for i in range(5):
        message = q.get()
        print(f"Agent 2 received: {message}")
        time.sleep(1)


q = queue.Queue()
t1 = threading.Thread(target=agent1, args=(q,))
t2 = threading.Thread(target=agent2, args=(q,))
t1.start()
t2.start()
t1.join()
t2.join()
