"""
Md Mubassirul Hoque 
Lab 11, class in Python (extra points)
"""
from lab11_functions import *

Student1= Students("Md",22)
grade1= Student1.add_grade("Physics",20)
grade2= Student1.add_grade("Mathematics",30)
Avg_grade = Student1.grade_avg()
Student1.print_avg()

Student2 = Students("Md",23)
Student2.print_avg()

Student3 = Students("James",30)
Student3.add_grade("Maths",100)
Student3.add_grade("Chemistry",100)
Student3.add_grade("Physics",89)
Student3.add_grade("Biology",37)
Student3.grade_avg()
Student3.print_avg()
