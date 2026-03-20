

'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car: Turning key / pressing button → engine starts")
    def stop(self):
        print("Car: Pressing brake → engine stops") 

class Bicycle(Vehicle):
    def start(self):
        print("Bicycle: Pushing pedals → moving")
    def stop(self):
        print("Bicycle: Pressing brakes → stopped")
# This works
c = Car()
c.start()
c.stop()

b = Bicycle()
b.start()
b.stop()

# This would FAIL (TypeError)
# v = Vehicle()   ← cannot 

#adding student
students = {"Alice": 85, "Bob": 91, "Charlie": 78, "Emma": 95}
print("Emma's score:", students["Emma"])
students["David"] = 92
students["Alice"] = 88           # updating Alice as example
print(students)

#countries and capital
capitals = {"Germany": "Berlin", "France": "Paris", "Italy": "Rome"}

for country, city in capitals.items():
    print(f"The capital of {country} is {city}")

#words separation
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
unique_words = set(words)
word_lengths = {word: len(word) for word in unique_words}

print(word_lengths)'''

#function
def greet_person(name):
    print("Hello ",name,", Welcome to Python!")
greet_person("John")
greet_person("Amara")
greet_person("David")    