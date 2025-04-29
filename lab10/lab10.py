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