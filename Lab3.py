Creating Base class Employee and defining constructor with private variables and Getting methods (encapsulation) and setting methods for salary

class Employee:
    def __init__(self,emp_id,name,salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary
        
    #Getting Methods    
    def get_emp_id(self):
        return self.__emp_id
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    #Settings Method
    def set_salary(self,salary):
        self.__salary = salary
        
Defining Child class Professor that inherites the property of Base class Employee and accessing the private variables through super() function in Child class

class Professor(Employee):
    def __init__(self,emp_id,name,salary,subject):
        super().__init__(emp_id,name,salary)
        
        self.subject = subject
        
    #Display function
    def display_details(self):
        print("Professor Details")
        print("------------------")
        print("ID:",self.get_emp_id())
        print("Name:",self.get_name())
        print("Salary:",self.get_salary())
        print("Subject:",self.subject)
        
Creating Object of professor(child) class

object = Professor(11,"Harry",90000,"Engineering Physics")
#Calling display function with object
object.display_details()
Professor Details
------------------
ID: 11
Name: Harry
Salary: 90000
Subject: Engineering Physics
File Handling for csv

import csv

data = [
    ['Name','Age','City'],
    ['Asha',22,'Kathmandu'],
    ['Ramesh',25,'Pokhara']
]

with open('output.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

data = {
    'Name':['Asha','Ramesh'],
    'Age':[22,25],
    'City':['Kathmandu','Pokhara']
}
Using Pandas library

import pandas as pd

df = pd.DataFrame(data)
df.to_csv('output1.csv',index=False)
Reading csv file

with open('output.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
['Name', 'Age', 'City']
['Asha', '22', 'Kathmandu']
['Ramesh', '25', 'Pokhara']
Reading csv files using pandas

import pandas as pd
output = pd.read_csv('output.csv')
print(output)
     Name  Age       City
0    Asha   22  Kathmandu
1  Ramesh   25    Pokhara
File handing with json

import json
  
data = [
    {"Name":"Asha","Age":22},
    {"Name":"Ramesh","Age":25}
]      

with open('output.json','w') as file:
    json.dump(data,file,indent=4)
File handling with txt

students = [
    "1, Ram, 85",
    "2, Sita, 90",
    "3, Hari, 78"
]

with open("students.txt",'w') as file:
    for student in students:
        file.write(student)
        
Read data from txt file

with open("students.txt", "r") as file:
    content = file.read()

print("\nReading data from file:")
print(content)
Reading data from file:
1, Ram, 852, Sita, 903, Hari, 78
Creating data and write to excel

import pandas as pd

# Create data
data = {
    "ID": [1, 2, 3],
    "Name": ["Ram", "Sita", "Hari"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Write to Excel
df.to_excel("students.xlsx", index=False)
Read excel file

import pandas as pd

df = pd.read_excel("students.xlsx")
print(df)
   ID  Name  Marks
0   1   Ram     85
1   2  Sita     90
2   3  Hari     78
