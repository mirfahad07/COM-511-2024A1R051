#write a python program to store one student data as a tuple: name, roll number, and marks, display grade based on marks

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student = (name, roll, marks)

print("Student data:", student)

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)
