"""
Md Mubassirul Hoque 
April 25, loops

"""

print("\n ----------------- example1: for loop as a counter -------------------")
# print Hello from 0 to 4 
for x in range (0,5):
    print(f"Hello ={x} ")

print("\n --------------- Example 2 : For loop in a list -----------")
fruits = ['apples', 'oranges', 'grapes', 'kiwis', 'pineapple']
for eachfruitindex in range(0,len(fruits)):
         print(f"fruit with index {eachfruitindex} = {fruits[eachfruitindex]}")

#alternative way to loop through a list
print("\n --- Alternative way to loop through a list")
for eachfruit in fruits:
       print(eachfruit)

print("\n --------------- Example 3 : For loop with different increments -----------")
# for loop to print from 2 to 30, with an increment of 3
for num in range (2,30,3):
       print(num)

print("\n --------------- Example 4 : For loop with different decrements -----------")
# for loop to print from 10 to 2, with a decrement of -2
for  num in range(10,0,-2):
       print(num)

print("\n --------------- Example 5 : For loop through a String-----------")
username = "Jes123"
for eachcharacter in username:
       print(eachcharacter)

print("\n --------------- Example 6 : Nested Conditional Statement: Count-----------")
# for loop to check how many negative numbers are in the list 
numbers = [5, -2, 0, 8, 9, -1]
negativecounter = 0 
for eachnumber in numbers:
       if eachnumber <0:
              negativecounter +=1 # same as negativenumber = negativenumber+1
            
# prompt result
print(f"There is/are {negativecounter} negative number/s")

print("\n --------------- Example 7 : Nested Conditional Statement: operation-----------")
# for loop to add all 'odd' numbers
sumodd = 0
for eachnumber in numbers :
       if eachnumber %2 ==1:
            sumodd += eachnumber
#prompt result 
print(f"The sum of all odd numbers is {sumodd}")

print("\n --------------- Example 8 : Break statement in a loop -----------")
# for loop to print from 0 to 10 (exclusive), and terminate the loop when it reaches to 5 
for n in range (0,10):
       if n==5:
              print("Counter reaches to 5")
              break
       else:
              print(n) 

print("\n --------------- Example 9 : Continue statement in a loop -----------")
# for loop to add numbers from 0 to 10 (exclusive), except 5 
sumall = 0
for n in range(10):
       if n==5 :
              print("Skipping 5")
              continue
       sumall += n
       print(n)
       print(f"\tsum = {sumall}") 

print("\n --------------- Example 10 : Else statement in a for loop -----------")
for n in range (6):
    if(n == 3): 
        break
    print(n)
else:
     print("Loop Completed")

print("\n --------------- Example 11 : While loop as a counter -----------")
# while loop to print from 0 to 5 (inclusive) ---> 0 1 2 3 4 5 
n = 0
while n<6:
      print(n)
      n += 1

print("\n --------------- Example 12 : While loop as a checkpoint -----------")
# while loop to collect and add numbers between -5 to 5
#  if the user enters a number that is not between -5 and 5, the while will terminate
sumusernumber = 0
while(True):
      number = int(input("Enter a number between -5 and 5 : "))
      if number <-5 or number >5 : #if not (5 >= number >= -5 )
            break
      sumusernumber += number

#prompt result
print (f"The total sum is = {sumusernumber}")

print("\n ----------- Example 13 : While loop as a counting operator -----------")
# while loop to count the even numbers in the list 
numbers = [2, 0, -5, 1, 8, -6, 7, -3]
index = 0
len_numbers = len(numbers)
evencount = 0
while index<len_numbers:
    if numbers[index]%2 == 0 and numbers [index] !=0:
        evencount += 1
    index +=1
else:
      print(f"There is/are {evencount} even numbers ")