#lab3 Data Wrangling Using Python

#import pandas

import pandas as pd

#TaskA Importing data
studentdata = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab3_DataWranglingUsingPython\Lab3_TaskA_CSVfile.csv")

#studentdata = pd.read_csv("C:\Lab3_TaskA_CSVfile.csv)
print(studentdata.head())   #Prints the first 5 rows of the imported data table
print(studentdata.tail())   #Prints the last 5 rows of the imported data table

#TaskB

#slicing
student_marks1 = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab3_DataWranglingUsingPython\Lab3_TaskB1_CSVfile.csv")
student_marks2 = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab3_DataWranglingUsingPython\Lab3_TaskB2_CSVfile.csv")
lasttworows = student_marks1.tail(2) #Passes two (2) rows of data from the bottom (tail)
firstthreerows = student_marks2.head(3) #Passes three (3) rows of data from the top (head)
print(lasttworows)
print(firstthreerows)

#Merging
merge = pd.merge(student_marks1,student_marks2) #merges the two data tables columns
print(merge)

"""
#Indexing
merge.set_index("Student_ID",inplace=True)  #Removing the index numbers
print(merge)    #Print the merged table 'merge' with index numbers removed
"""
"""
#Renaming the column header
merge= merge.rename(columns={"Drama":"Social_Studies"}) #Renaming the drama column to social studies
print(merge)
"""
#Concatenation 
student_marks3= pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab3_DataWranglingUsingPython\Lab3_TaskB3_CSVfile.csv")
Concat1= pd.concat([student_marks2,student_marks3]) #joining two data tables rows together into one
Concat1.set_index("Student_ID", inplace=True)  #removing the index numbers(Setting index as "student ID")
print(Concat1)

#Data Munging 
cohort2 = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab3_DataWranglingUsingPython\Lab3_TaskB3_CSVfile.csv", index_col=0)
cohort2.to_html('cohort2.html') #Converts the file to specified format (Html)
cohort2.to_csv('cohort2.csv')   #Converting to (CSV)

#TaskC Statistical information 
from statistics import mean 
Maths_mean = mean(student_marks1['Maths'])
print("Mean grade for maths = ", Maths_mean)

from statistics import median 
Maths_median = median(student_marks1['Maths'])
print("Median grade for maths = ", Maths_median)

from statistics import variance
Science_variance = variance(student_marks1['Science'])
print("Variance = ", Science_variance)

#TaskD Plotting

import matplotlib.pyplot as plt #importing plttting package
from matplotlib import style
style.use("fivethirtyeight")    #Theme / style of the graph

merge.plot()    #define data table to plot
plt.show()  #Display graph

Results=pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab3_DataWranglingUsingPython\Lab3_TaskB4_CSVfile.csv", index_col=0)
Results=Results.set_index(["Student_Name"])
sd= Results.reindex(columns=['Percentage_Sem1','Percentage_Sem2'])
#merge= merge.rename(columns={"Drama":"Social_Studies"}) #Renaming the drama column to social studies

print(sd)
db=sd.diff(axis=1)
print(db)

db = db.reindex(columns=['Percentage_Sem2'])
db = db.rename(columns={'Percentage_Sem2':'Difference'})

#db.plot(kind='bar')
#plt.show()
