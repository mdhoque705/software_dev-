"""
Md Mubassirul Hoque
April 20, Introduction Python
"""

# Single comment. This line WILL NOT run
print("\n----- Example 1: String Characters -----")
print("\tGood Morning! \nThis is my first \"Python\" code!")

print("\n----- Example 2: Data type -----")
print(f"Data type of 3.56 = {type(3.56)}")

print(f"Data type of -25 = {type(-25)}")
print(f"Data type of 'Hello World!'= {type('Hello World')}")
print(f"Data type of character '$' = {type('$')}")
print(f"Data type of False = {type(False)}")

print('\n---------- Example 3: Variables---------')
#declare variables

number1 = 10.4
number2 = 10.9
username = "Peter Pan"
add_numbers= number1 + number2
is_raining = True

#Prompt results

print(f"{username} , the sum of {number1} and {number2} is {add_numbers}")
print(f"Is it raining today? = {is_raining}")

print("\n------ Example 4:Assigning values to multiple variables ------")
#declare multiple variables
item1, item2, item3 = "apples", "25", "False"
print(f"item 1 = {item1}, item 2 = {item2}, item 3 = {item3}")
#Declare Multiple variables with same values
score1 = score2 = score3 = 90
print(f"Score 1 = {score1}, Score 2 = {score2}, Score 3 = {score3}")


print('\n------ Example 5: input command -----------')
print('Enter Username:')
Username = input()
print(f'Collected Username = {Username}')

# Cast from string to integer
luckynumber = int(input("Enter a lucky number: "))
print(f"Lucky Number = {luckynumber}")

#double the lucky number. cast from string to integer 
doublelucky = int(luckynumber)*2
print(f"Doubled Lucky Number = {doublelucky}")

#Cast from integer (or float) into string 
tirplenumber = str(doublelucky) * 3
print(f"Tripled the Casted Number = {tirplenumber}")

# Cast Integer to bool value 
# 0 = False, any other number = True 
completed_task= -20
print(f"Completed Task = {bool(completed_task)}")

print('\n---------- Example 6: Arithmetic Operators---------')
num1 = 5
num2 = 9


print(f"The sum of {num1} and {num2} is {num1+num2}")
print(f"Difference between {num1} and {num2} is {num1-num2}")
print(f"Product of {num1} and {num2} is {num1*num2}")
print(f"The quotient of {num1} and {num2} is {num1/num2} ")
print(f"The modulus(remainder) of {num1} and {num2} is {num1%num2} ")
print(f"The integer of quotient of {num1} and {num2} is {num1//num2} ")
print(f"The result of base {num2} to the power of 3 is {num2**3}")

print('\n---------- Example 7: Finding the hypoteneus---------')
# Declare and assign values 
x = float(input("Enter Side 1:"))
y = float(input("Enter Side 2:"))
#calculate the hypoteneus
hyp = (x**2 + y**2)**0.5
#Prompt result 
print(f"The hypotenuse of {x:0.1f} and {y:0.1f} is {hyp:0.3f}")

print('\n---------- Example 8: Assignment Operators---------')
n = 20
print(f"number =       {n}")
# assignment operator + 
n+=3
print(f"number+3 = {n}")

#assignment operator -
n-=4
print(f'Updated number= {n}')

#assignment operator *
n*=2
print(f"Updated Number = {n}")

#assignment operator /
n/=3
print(f"Updated Number = {n}")

#assignment operator //
n//=2
print(f"Updated Number = {n}")

#assignment operator **
n**=2
print(f'Updated Number = {n}')

# modulus or remainder 
n%=5
print(f"Updated number = {n}")

print('\n---------- Example 9: Comparison Operators---------')
n1 = 10 
n2 = 3 
n3 = 7

compare1 = n1==n2 
compare2 = n1==(n2+n3)

print(f"is n1 equal n2 ?  {compare1}")
print(f"is n1 = n2+n3 ? {compare2}")

compare3 = n1>n2 
compare4 = n2<=n3

print(f"is n1 greater than n2 ? {compare3}")
print(f" is n2 less than or equal to n3 ? {compare4}")

print('\n---------- Example 10: string Indexing---------')
username = "peterpan123"
# positive indexing 
print(f'The fifth character = {username[4]}')

# negative indexing 
print(f"The fifth last character = {username[-5]}")

print('\n---------- Example 11: string slice---------')
# slice from the begining to the 4th character 
print(f"Slice from beginning to 4th Character = {username[4]}")
# slice from the fifth character to the end 
print(f"Slice from the 5th character to the end = {username[6:]}")

# slice from the 3rd character to the 8th character 
print(f"Slice from 3rd to 8th = {username[2:8]}")

# slice from the 4th to the 6th character using negative indexing 
print(f"Slice from 4th to 6th using negative index = {username[-8:-5]}")

print('\n---------- Example 12: Total Characters in a String (len)---------')
print(f"The username has = {len(username)} characters")