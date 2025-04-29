"""

Md Mubassirul Hoque 
April 24, Conditional Statement


"""

print("\n-------- Example1 and example 2 : if statement ----------")
age = 20
agecode = 123

if age>= 21:
    print("You are an adult")
    agecode = 200
else:
    print("You are under 21!")
    agecode = 100

print(f"After the if statement, agecode = {agecode}")

print("\n-------- Example 3: Multi statement ----------")
age = 50 
if 0 <=age< 21:
    print("You are a Minor !") 
elif 21 <= age < 65:
    print("You're an Adult !")
elif 65 <= age <130:
    print("You're a senior citizen !")
else:
    print("Unable to read age !")

print("\n-------- Example 4: And Operator ----------")
temperature = 80
humidity = 100

if 70<=temperature<=90 and humidity < 80:
    print("The weather is pleasant")
else:
    print("The weather is not ideal")

print("\n-------- Example 5: Or Operator ----------")
day = "Monday"
is_holiday= True

if day == "saturday" or day == "sunday" or is_holiday:
    print("You can relax today")
else:
    print("It is a workday") 

print("\n-------- Example 6: nested conditional statement ----------")
number = int(input("Enter a Number: "))
if (number>=0):
    if number==0:
        print("The number is zero")
    else:    
        print(f"{number} is positive")
else:
    print(f"{number}is negative")

print("\n-------- Example 7: nested conditional statement ----------")
#username validation. username must have 3+ characters
username = input("Enter a username: ")
username = username.strip()
len_username = len(username)
if len_username >= 3:
    print(f"{username} has 3+ character")
    index_widespace = username.find(" ")
    if index_widespace == -1:
        print(f"{username} is valid")
    else:
        print(f"Username can not have wide space")
else:
    print(f"{username} is INVALID. Username must have 3+ characters")

print("\n-------- Example 8: match-case statement ----------")
response_code = 204 

match response_code:
    case 400:
        print(f"Code = {response_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code = {response_code}. Server refused to send back")
    case 404:
        print(f"Code = {response_code}. Server cannot find")
    case _ :
        print("INVALID CODE")




#Exercise 
print("\n------------ Lab 9: Exercise -------------")
grade1 = float(input("Enter your Grade 1: "))
if grade1<0 or grade1>100:
    print("INVALID GRADE 1")
else:
    grade2 = float(input("Enter your Grade 2 : "))
    if grade2<0 or grade2>100:
       print("INVALID GRADE 2")
    else:
       Average = (grade1 + grade2)/2

       if 90 <=Average <= 100 :
            print(f"For the average of {Average : 0.2f}, your GPA is A ")
       elif 70 <=Average <= 89.99 :
            print(f"For the average of {Average : 0.2f}, your GPA is B ")
       elif 60 <=Average <= 69.99 :
            print(f"For the average of {Average : 0.2f}, your GPA is C ")
       elif 0 <=Average <= 59.99 :
            print(f"For the average of {Average : 0.2f}, your GPA is FAIL ")
       else:
            print("UNDEFINED")
