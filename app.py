import math

#calculate the hypothenus of a triangle

a = int(input("Please enter the angle of the first sight: "))
b = int(input("Please enter the angle of the second sight: "))
hypothesis = math.sqrt(math.pow(a,2)+math.pow(b,2))
print(f"The hypothenus of the triangle is  {round(hypothesis, 2)}")