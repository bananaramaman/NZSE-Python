#print("Hello World")

#variables

from ast import Num
from lib2to3.pgen2.token import NAME
import numbers
from re import I
from telnetlib import NEW_ENVIRON
from tkinter.tix import InputOnly
from types import prepare_class

"""
#character1="Darren"
#character2="python"
#print("My name is " + character1 + ",")
#print("I like " + character2)

#print("Welcome to this course. \n\"SWD503\" \nThis is //***AWESOME***//")
#phrase="Welcome to this course. \n\"SWD503\" \nThis is //***AWESOME***//"
#print(phrase.upper())

#phrase1="Darren Burton"
#print(phrase1[0])

#print(4+3)
#print(3.14-3)
#print(11/4)
#print(11%4)

#Further equations

#print(abs(-5))
#print(pow(5,3))
#print(max(4,7,8,9,2,6))
#print(round(3.456))
"""
from math import *
"""
#print(floor(4.7))
#print(ceil(4.1))
#print(sqrt(64))

#taking user input

#name = input("please enter your name: ")
#dob = input("Enter your date of birth")
#print("Hello " + name +"!", "your date of birth is "+dob+".")

#num1= input ("Enter a number: ")
#num2= input ("Enter another number: ")
#result = float(num1) + float(num2)
#print("The addition of these numbers is: ", result)

#working with lists

studentlist = ["Charlie","Sophia","Robert","Michael","Alex","Rachel","Terrence"]
#print(studentlist)

#varietylist = ["Robert", 5.7,"Machinist",23.50]
#print (varietylist)

#print(studentlist[1])
#print(studentlist[0])

#print(studentlist[-1])
#print(studentlist[1:5])

#studentlist[0]="Charles"

#print(studentlist)

#list functions

#newenrolments= ["Jeremy","Jessica","Sylvia","Bob"]      #define list to be added
#studentlist.extend(newenrolments)   #add new list to current list
#studentlist.append("Ian")       #add entry to end of list
#studentlist.insert(2, "Poppy")      #insert entry at defined index location
#print(studentlist)


#studentlist.pop(4)      #pop/remove entry index
#print(studentlist.index("Sophia"))      #displays index of defined entry
#studentlist.remove("Bob")   #Remove entry
#print(studentlist)

#studentlist.sort()      #sorts a list by alphabetical or numbers in ascending order
#print(studentlist)

#studentlist2 = studentlist.copy()   #copies the original list to studentlist2 

#mylottonumbers= [34,4,6,17,27,35]
#print(mylottonumbers)   
#mylottonumbers.sort()   #sorts in ascending order
#print(mylottonumbers)
#mylottonumbers.reverse()    #reverses the list
#print(mylottonumbers)

#Tuples

#coordinates=(2,4)
#print(coordinates)
#coordinates1= [(2,6),(3,5),(8,26),(15,17)]
#print(coordinates1)

#Functions
"""
"""
def say_my_name(name, surname): #define functions 
    print("Welcome "+name+surname)  #prints returned data

print("Hello ")
say_my_name("Darren ","Burton")
print("Have a nice day")
"""
"""
def cube(a):
    return a*a*a

num = input("please enter a number: ")
result = cube(float(num))
print(result)
 """


"""
#If statement
studentmarks = 75
if studentmarks >= 50:
    print("Pass")
else:
    print ("Fail")

studentattendance =50
if studentattendance >= 80 and studentmarks >= 50:
    print("Pass")
elif studentmarks>=50 and studentattendance <80:
    print("Results withheld")
"""
"""
# if loops
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(17,14,25))
"""

"""
i = 1
while i <= 10: #While loop incrementing (i) value
    print(i)
    i=i+1
    
x = 1
while x <= 10:          #while loop with incrementing (i) with power of equation
    print(pow(2,x))
    x=x+1

studentlist = ["Charlie","Sophia","Robert","Michael","Alex","Rachel","Terrence"]
for i in studentlist:       #(i) increments and prints values of list
    print(i)

for i in range(15):     #(i) increments separate from previous while loop 
    print(pow(2,i))

for i in [1,3,5]:       #defines set numbers for which to represent (i), then print power of 2,i
    print(pow(2,i))

myl=(1,3,5)         #storing set numbers in variable for use in for loop 
for i in myl:
    print (pow(2,i))
"""
"""
#Exponent function
print(5**2)     #python method of defining base number and 'power'number

def raise_to_power (base_num,pow_num):  #defining base and power number equation using range
    result=1
    for i in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(5,3))  #definition of base and power numbers (not related to top example)
"""
"""
#Grid (similar to 3d Array in C#)
number_grid= [(1,2,3,),(3,4,5),(6,7,8),(1)]

#print(number_grid[0][0])    #print grid set index number 0 and print index number 0 value of that set
#print(number_grid[2][0])    #print grid set index number 2 and print index number 0 value of that set
#print(number_grid[1][1])    #print grid set index number 1 and print index number 1 value of that set 

print(len(number_grid))
#nested loop
for i in number_grid:
    for j in i:
        print(j)
"""
"""
#Try/Except

#try:
 #   num= int(input("Enter a number: "))
  #  print(num)
#except:
 #   print("invalid Input")

try:
    num1= int(input("Enter an integer: "))
    val = 10/num1
    print(val)
except ZeroDivisionError:
    print("Attempted to divide by zero...")
except ValueError:
    print("invalid input")
"""

"""
#reading files

studentmarks = open("student.txt","r")
print(studentmarks.read())

#writing on files
studentmarks = open("student.txt", "a")
studentmarks.write("78 99 100")
studentmarks.write("\n 5 6")
studentmarks = open("student.txt", "w")
studentmarks.write("All student marks haave been deleted")


studentmarks = open("student.txt","r")
print(studentmarks.read())
"""

#modules 
import MyFirstPythonPractice
print(MyFirstPythonPractice.raise_to_power(5,3))
