# Write a program to:
# Calculate the total marks obtained by each student.
# Store the results in a new file total_marks.txt in the format:
# Use class to store the marks, create a method to calculate total marks and store the marks with student name as dictionary
import json
class Student:
    def __init__(self, name, english, nepali, science, social, maths, optMaths, computer):
        self.name = name
        self.english = english
        self.nepali = nepali
        self.science = science
        self.social = social
        self.maths = maths
        self.optMaths = optMaths
        self.computer = computer
        
    def totalMarks(self):
        return self.english + self.nepali + self.science + self.social + self.maths + self.optMaths + self.computer


students_data = {} 

name = input("Name: ")
try:
    eng = float(input("English: "))
    nep = float(input("Nepali: "))
    sci = float(input("Science: "))
    soc = float(input("Social: "))
    maths = float(input("Maths: "))
    optMaths = float(input("Optional Maths: "))
    com = float(input("Computer: "))
        
    obj = Student(eng, nep, sci, soc, maths, optMaths, com)
    total = obj.totalMarks()
    students_data[name] = total
    print(f"Total Marks: {obj.totalMarks()}")  

except:
    print("Invalid input.")

file=open("total_marks.txt", "w")
for name, total in students_data.items():
    data={name:total}
    json_data=json.dumps(data)
    file.write(json_data+",")
    file.close()

