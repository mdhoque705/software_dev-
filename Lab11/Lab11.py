"""

Md Mubassirul Hoque 
April 27, Python Applications

"""
# import all from file "lab11_functions"
from lab11_functions import*

#import 'math' module 
import math

print("\n------------ Example 1: Python Dictionary -----------")
# create a dictionary
car = {
    "brand": "Ford",
    "model":"Mustang",
    "year" : 1964.
}
# print a complete dictionary 
print(car)
# to access items in a dictionary we use [], where goes the key's name 
print(f"The year of the car is = {car["year"]}")

# Update the value of the key 
car["year"] = 1980
print(f"The year of the car was upadted to = {car['year']}")

#add key:value pair 
car["color"] = "red"
print(car)

print("\n Loop through each key in a dictionary")
for k in car :
    print(k)

print("\n Loop through each value in a dictionary")
for k in car :
    print(car[k])
print("\nLoop through each pair in the dictionary")
for k in car:
    print(f"{k} has value = {car[k]}")

print("\n--------------- Example 2: Python Dictionary Application -----------")
# given the following list, create a dictionary that will count the number of items that a word appears in the string 
# create a dictionary to organize the words asthe keys, and the number of occurency of the word as the value of the key. 
phrase = "to be or not to be"
print(f"The original phrase is = {phrase}")
phrase_split = phrase.split()
print(f"splitted phrase = {phrase_split}")
# create the dictionary 
word_counnt_dict = {}
#loop to each word in the lsit 
for word in phrase_split:
    if word in word_counnt_dict:
        word_counnt_dict[word] +=1
    else:
          word_counnt_dict[word] = 1
# print result 
print("Result of the dictionary: ")
for w in word_counnt_dict:
    print(f"'{w}'= {word_counnt_dict[w]}")

print("\n--------------- Example 3: Function that doesn't return values -----------")
# run function 'Greeting'
greeting()

print("\n--------------- Example 4: Function with parameters-----------")
# call function "printusername"
printusername("Mubassir")

print("\n--------------- Example 5: Function with Default parameters-----------")

user_country("" , "")

print("\n--------------- Example 6: Function with Return Value -----------")

num1 = 2
num2 = -6 
prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}") 

prod1 = product(num1)
print(f"The product is = {prod1}")

prod1 = product()
print(f"The product is = {prod1}")

print("\n--------------- Example 7: Boolean Fucntions -----------")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} multiple of 3? {checknum2}")

print("\n--------------- Example 8: Composition Fucntions -----------")
# test collectnum()
# number = collectnum()
# print(number)

# test sumnumbers()
sumall = sumnumbers(3)
printresults(sumall) #printresults(sumnumbers(3))

print("\n--------------- Example 9: Built-in Fucntions -----------")

r=2 
a= areacircle(r)
areaprint(a,r)

print("\n--------------- Example 10: Try-Except -----------")

r1 = ratio_hour(0)
r2 = ratio_hour(3)
r3 = ratio_hour("Peter")

print("\n--------------- Example 11: CLASSES -----------")
# create an instant of the class 
user1 = Myclass()
print(f"An instance of the Class = {user1}")
# call the class property
user1id = user1.id
print(f"user 1 id = {user1id}")
# call the class method 
user1msg = user1.msg()
print(f"User 1 message = {user1msg} ")

print("\n--------------- Example 12: Instantiation Classes -----------")

# create an instant of the class 
paircomplexnumber = Complexnumber(2,3)
# call the instance object 'r' of the class
real = paircomplexnumber.r
print(f"The real part is {real}")


print("\n--------------- Example 13: Classes Application -----------")
# create an instant of the class
car1 = Car("Tesla","S", 2023)
# call property "odometer_reading"

car_reading = car1.odometer_reading
print(f"The Car mileage is = {car_reading}")

#call method 'get_car_description'
print(car1.get_car_description())

#call method 'read_odometer'
print(car1.read_odometer())

#update the odometer to mileage = 10 
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer())

# add 20 miles to the odometer 
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer(-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())