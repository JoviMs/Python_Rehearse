
''' MyNumber = [1, 2, 3, 4, 5]
MyNumber2 = [1, 2, 3, 4, 5]

My3 = [MyNumber, MyNumber2]
print(My3)
My3.MyNumber.append(6)
 print(json.dumps(My3, indent=4)) '''

''' person = ("Alice", "25", "Berlin")
name = person[0]
age = person[1]
city = person[2]
print("Name:", name)
print("Age:", age)
print("City:", city)
print(" f{name} is {age} years old and lives in {city}. ") '''

'''count_list = [1, 2, 3, 4, ]

sum = 0
for my_counter in range(10):
    if my_counter != 0 and my_counter < 5:
        print("condition met")
        break
    print(my_counter)
    sum = sum
print(sum)

exit(0)'''

'''''
x = [1,2,3,4,5]

min_val = x[0]
for i in x:
    if i < min_val:
        min_val = i
print("Minimum value is:", min_val)'''''

''''
my_addressbook = [
    {
        "name": "John Doe",
        "phone": "123-456-7890",

    },
    {
        "name": "Jane Smith",
        "phone": "987-654-3210",
    },
    {
        "amen": "Emily Johnson",
    },
    {
        "name": "Michael Brown",
        "phone": "555-555-5555",
    },
]
searchterm = input("Enter name to search: ")
for address in my_addressbook:
    if "name" in address.keys():
        if address["name"] == searchterm:
            print("Found:", address)
    else:
        print("Not found")

exit(0) '''

'''x = 22
for i in range(2, x+1):
    print_it = True
    for j in range(2, i):
        if i % j == 0:
            print_it = False
    if print_it:
        print(i)
exit(0) '''

'''

# 1) Write Python code to add the odd numbers
N = int(input("Enter a value for N: "))
sum_odd = 0
for i in range(1, N+1, 2):
    sum_odd += i
print(f"The sum of odd numbers up to {N} is: {sum_odd}")

# 2)Write a program to find the lowest number from a list of numbers
numbers = [22, 53, 345, 7, 3, 22, 56, 13]
min_number = numbers[0]
for num in numbers:
    if num < min_number:
        min_number = num
print("The lowest number is:", min_number)

# 3)Write a python program to print the Fibonacci series’ first 20 elements : 0,1,1,2,3,5,8……
a, b = 0, 1
count = 0
while count < 20:
    print(a, end=', ' if count < 19 else '\n')
    a, b = b, a + b
    count += 1

# 4)Write a Python script to print the first ten Mersenne Numbers
for i in range(1, 11):
    mersenne_number = (2 ** i) - 1
    # mersenne_numbers.append(mersenne_number)
print("The first ten Mersenne numbers are:", mersenne_number)

# 5) Write a Program to print the following pattern:
pattern = "*"
for i in range(1, 5):
    # print(pattern * i)
    pattern += "**"
    print(pattern)


# 6) A year is a leap year if it is divisible by 4.
years = int(input("Enter number of years: "))
if years < 0:
    print("Invalid input")
elif years % 4 == 0:
    print(f"{years} is a leap year")
elif years % 100 == 0:
    print(f"{years} is not a leap year")
elif years % 400 == 0:
    print(f"{years} is a leap year")
else:
    print(f"{years} is not a leap year")

# 7) Write a program to input length of 3 sides of a triangle

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))


if a+b > c and a+c > b and b+c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


# 8) Write a short program to input a digit and print it in words.
numbers = {
    0: {
        "en": "Zero",
        "de": "Null",
        "Li": "Moh"
    },
    1: {
        "en": "One",
        "de": "Eins",
        "Li": "mba"
    },
}

lang = input("Enter language (en/de/Li): ")
number_in = int(input("Enter a digit (0-9): "))

print(numbers[number_in][lang])


# 9) Given an input check if it is a palindrome or not.
teststring = input("Enter a string: ")
if teststring == teststring[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 10) Write a Python script to input temperature.
temperature = int(input("Enter temperature in Celsius: "))
celsius_to_fahrenheit = (temperature * 9/5) + 32
print(f"{temperature}°C is {celsius_to_fahrenheit}°F")
fahrenheit_to_celsius = (temperature - 32) * 5/9
print(f"{temperature}°F is {fahrenheit_to_celsius}°C")
'''
''''
class Employee:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employees(Person):
    def __init__(self, name, age, job_role):
        super().__init__(name, age)
        self.job_role = job_role
    def role(self):
        print(f"{self.name} works as a {self.job_role}")
    
    def display(self):
        super().display()
        print(f"Hello my name is {self.name} and I am {self.age} years old.")
        
x1 = person("Bob")
x1.display()
x2 = Employees("Alice", 30, "Developer")
x2.display()         
print (x1) 
exit(0) '''

'''
#6)
class Address:
    def __init__(self, fname, lname, email):
        self.email = email
        
    def display(self):
        print(f"First Name: {self.fname}, Last Name: {self.lname}, Email: {self.email}")  
class AddressBook:
    def __init__(self, name):
        self.name = name
        self.addresses = []
    def contact_add (self, fname, lname, email):
        self.addresses.append(Address(fname, lname, email))
    def contact_list(self):
        for contact in self.addresses:
            #contact.display()   
            #print("first_name: {self.fname}, last_name: {self.lname}, email: {self.email}")
                        
         def contact_search(self, searchterm):
          for contact in self.addresses:
            if contact.fname == searchterm or contact.lname == searchterm:
                print("Contact found:")
                contact.display()
                break         
   
ab = AddressBook("My Address Book")
ab.contact_add("John", "Doe", "sbdsjdujd@eeds.com" )
ab.contact_add("Jane", "Smith", "sijss@djwkc.com")

exit(0) '''

'''
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass     
class Car(vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")    
c1 = Car()
c1.start_engine()
v1 = vehicle()  # This will raise an error 
'''
'''
# 1) Write a function greet_user which takes 2 parameters first_name, last_name and prints apersonalized message like : “Hello, Bob Ross! Welcome back!”If the last name is not given it should print the same message without the lastname
def greet_user(first_name, last_name=""):
    if last_name:
        print(f"Hello, {first_name} {last_name}! Welcome back!")
    else:
        print(f"Hello, {first_name}! Welcome back!")


greet_user("Bob", "Ross")

# 2) Write a function find_max(a,b,c) that returns the largest of 3 numbers without using Python’sbuilt – in max()


def find_max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num


print("The largest number is:", find_max(10, 25, 15))
# 3) Write a function average(numbers) that takes a list of numbers and returns their average.If the list is empty, return 0


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print("The average is:", average([10, 20, 30, 40, 50]))
# 4) Write a function filter_even(numbers) that takes a list of integers and returns a new listcontaining only the even numbers.


def filter_even(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# 5) Write a recursive function factorial(n) that returns the factorial of n. If n < 0 then return “InvalidInput”


def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial is:", factorial(5))
# 6) Write a function write_lines(filename, lines) that takes a filename and a list of strings and writeseach string on a new line


def write_lines(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')


lines_to_write = ["Hello, Class!", "This is a test.", "Writing to a file."]
write_lines("output.txt", lines_to_write)
# 7) Write a function count_words(filename) that reads a text file and prints the number of words in it


def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)


print("Number of words:", count_words("output.txt"))
# 8) Write a function longest_length(filename) that reads a file and prints the line with the maximumlength


def longest_length(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        max_length_line = max(lines, key=len)
        return max_length_line.strip()


print("The longest line is:", longest_length("output.txt"))

# 9) Write a function reverse_file(input_file, output_file) that reads all lines from input_file andwrites them in reverse order to output_file.


def reverse_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    with open(output_file, 'w') as outfile:
        for line in reversed(lines):
            outfile.write(line)


reverse_file("output.txt", "reversed_output.txt")
# 10) Write a function word_frequency(filename) that reads a text file and prints how many timeseach word appears (case insensitive -> the and THE are the same word)


def word_frequency(filename):
    with open(filename, 'r') as file:
        content = file.read().lower()
        words = content.split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        return frequency


print("Word frequency:", word_frequency("output.txt"))

'''


import tkinter as tk
def move_left(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    print("Left arrow key pressed")
    if x1 > 0:
        canvas.move(spaceship, -10, 0)


def move_right(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    print("Right arrow key pressed")
    canvas.move(spaceship, 10, 0)


'''
root = tk.Tk()
root.title("Simple GUI")
root.geometry("200x100")

canvas = tk.Canvas(root, width=800, height=600, background="blue")
canvas.pack()

canvas.create_rectangle(400, 500, 550, 550, fill="red", outline="black")
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)'''

'''def hello():
    my_name = my_input.get()
    print(f"Hello, welcome {my_name}!How are you today?")
    my_label.config(text=f"Hello, welcome {my_name}!How are you today?")
'''


'''x1 = y1 = 0


def start_rectangle(event):
    global x1, y1
    x1, y1 = event.x, event.y


def finish_rectangle(event):
    canvas.create_rectangle(x1, y1, event.x, event.y)


def print_xy(event):
    print("Mouse clicked", event)
    pass


tmp_rectangle = None


def draw_rectangle(event):
    global tmp_rectangle
    if tmp_rectangle != None:
        canvas.delete(tmp_rectangle)
        tmp_rectangle = None
    tmp_rectangle = canvas.create_rectangle(x1, y1, event.x, event.y)


def shoot(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    bullet = canvas.create_rectangle(x1+48, 535, x1+52, 545, fill="yellow")
    print("shoot")
    bullet_move(bullet)


def bullet_move():
    print("move bullet")
    canvas.move(bullet, 0, -10)

    bullet_coords = canvas.coords(bullet)
    x1, y1, x2, y2 = bullet_coords
    if y1 > 0:
        root.after(20, bullet_move, bullet)
    else:
        canvas.delete(bullet)


root = tk.Tk()
root.title("Simple GUI")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, background="white")
canvas.pack() '''

'''root.bind('<Button-1>', start_rectangle)
root.bind('<ButtonRelease-1>', finish_rectangle)
root.bind('<Button-3>', print_xy)

canvas.bind('<B1-Motion>', draw_rectangle)
spaceship = canvas.create_rectangle(375, 500, 425, 550, fill="red", outline="black")
root.bind('<space>', shoot)

root.bind('<Left>', move_left)
root.bind('<Right>', move_right)
root.bind('<space>', shoot)



my_input = tk.Entry(root)
my_input.pack(pady=20)

button = tk.Button(root, text="Greet Me", command=hello)
button.pack(pady=20)
button2 = tk.Button(root, text="Exit", command=root.quit)
button2.pack(pady=20)
button3 = tk.Button(root, text="Close", command=root.destroy)
button3.pack(pady=20)

my_label = tk.Label(root, text="Enter your name:", bg="yellow", fg="blue")
my_label.pack()


root.mainloop()'''
