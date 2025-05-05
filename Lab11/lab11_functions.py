"""
Md Mubassirul Hoque 

April 27, Functions

"""

import math
#example 3 
def greeting():
    print("Welcome to functions!")

#Example 4 
def printusername(username):
    print(f"Welcome to Functions {username}")

#Example 5, function with default parameters
def user_country(username = "(no name)", country = "unknown country"):
    print(f"{username} is living in {country}")
    return

#Example 6, Functions that returns a value 
# function that takes two numbers and returns the product
def product(n1 = 0,n2 = 1):
    return n1*n2

#Example 7: Boolean Function
#Function to check if a number is multiple of 3 

def multiple3(n):
    if n%3 == 0 and n!= 0:
        return True
    else:
        return False 
        
#Example 8 : Composition Function
# define function to collect, validate, and return a number between 1 and 9
def collectnum():
    n = float(input("Enter a number between 1 and 9(inclusive):  "))
    #validate the number 
    while(not(1 <= n <= 9)):
        n = float(input("Enter the number again: "))
    return n

# function that adds 'totalnumbers' amount of numbers and returns the sum of the numbers 
def sumnumbers(totalnumbers=0):
    sum = 0
    for n in range (totalnumbers):
        sum += collectnum() # composition functions
    return sum

#function to print results 
def printresults(totalsum):
    print(f"Sum of all numbers is = {totalsum}")

# Example 9
# define a function to calculate and return the area of a circle 
# formula = radius^2 * pi
def areacircle(radius):
    a = math.pow(radius,2) * math.pi
    return round (a,2)

#function to print results
def areaprint(area, radius=0):
    print(f"The area of a circle with {radius} radius is {area}")

# function to return the quotient of two numbers (hours)
def ratio_hour(hour):
     try:
       dayhour = 24
       r = dayhour/hour
     except ZeroDivisionError:
         print('ZERO EXCEPTION')
         print("Number can't be divided by Zero")
         return 0
     except ValueError:
         print('VALUE EXCEPTION')
         print("Number was not provided")
         return 0 
     except:
       print("GENERAL EXCEPTION")
       print("There was an error in the division")
     else:
         print("DIVISION IS FINE")
         return r
     finally:
         print("Process Completed !")

#example 11
#defining a class name 'Myclass'
class Myclass:
    #property(attribute)
    id = 12345

    #method
    def msg(self):
        return "Welcome to Python Class"
    
#Example 12 
class Complexnumber():
    #instantiate of the class
    def __init__(self, realnumber, imgnumber ):
        self.r = realnumber
        self.i = imgnumber

#Example 13 
class Car:
    #instantiate of the class
    def __init__(self,make, model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year
    
    # set property 'odometer'
    odometer_reading = 0 

    #method to return description of the car 
    def get_car_description(self):
        return f"{self.carmake} with model {self.carmodel} was made on {self.caryear}"
    
    #method to read the odometer 
    def read_odometer(self):
      return f"This car has {self.odometer_reading} miles on it"
    
    #method to update the odometer 
    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print('Odometer CAN\'T roll back ')

    #method to add miles into the odometer 
    def increment_odometer(self,miles):
        if miles>0:
            self.odometer_reading += miles
        else:
            print("Can't add negative miles")

#Exercise 
class Students:
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
        self.grade = {}
        print(f"The name of the student is {self.name} and their age is {self.age}")
        

    def add_grade(self,subject="Unknown",grade=0):
        self.grade[subject] = grade 

    def grade_avg(self):
        if len(self.grade) == 0:
            print ("Write Valid subject and grade")
        else:
            return sum (self.grade.values())/len(self.grade)

    def print_avg(self):
        print(f"Your Average grade for {len(self.grade)} subjects is = {self.grade_avg()}") 




