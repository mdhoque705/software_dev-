"""
Md Mubassirul Hoque

28th April 2025 
""" 



colors = ['red', 'orange', 'olive', 'magenta', 'green']

color_input = input("Enter a color's name: ").strip().lower()
gotit= False
for colornames in colors:
    if color_input == colornames:
        gotit = True
        break
if gotit:
    print(f"{color_input} Color was found in the list")
else:
    print(f"{color_input} was not fount in the list")



