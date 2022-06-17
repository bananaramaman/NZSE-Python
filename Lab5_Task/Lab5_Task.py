from hashlib import new
from turtle import pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#importing data
studentdata = pd.read_csv(r"C:\Users\User\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab5_ExploratoryAnalysisUsingPython\Lab5_StudentsPerformance.csv")
print(studentdata.head(5))

#Data Exploration 
"""
#print(studentdata.columns)
#print("\n")
#print(studentdata.shape)    #(Rows, Columns)
#print("\n")
#print(studentdata.describe())
print("\n")
#print(studentdata.isnull()) #indicates the null values 
#print(studentdata.isnull().sum()) #Gives a sum of all null values
print(studentdata.nunique())    #prints the number of unique values

#print(studentdata['parental level of education'].unique())      #list the individual unique values
#print(studentdata['lunch'].unique())
"""
#Data Cleaning

Newstudentdata=studentdata.drop(['race/ethnicity', 'parental level of education'], axis=1)  #removes the following columns from the data table axis=1 defines the axis to remove from
#print(Newstudentdata)

#Relationship Analysis
"""
correlation= Newstudentdata.corr()
sns.heatmap(correlation, xticklabels=correlation.columns,yticklabels=correlation.columns,annot= True)   #defines the layout of heatmap graph, (annot=True, sets annotations to TRUE)
plt.show()
"""
#Pairplot
#sns.pairplot(Newstudentdata)
#plt.show()

#Scatterplot
"""
#sns.relplot(x="math score",y='reading score',data=Newstudentdata)
#plt.show()

#sns.relplot(x="math score",y='reading score',hue='gender',data=Newstudentdata)
#plt.show()
"""

#Histogram plot
"""
#sns.distplot(Newstudentdata['math score'])
#plt.show()
#sns.distplot(Newstudentdata['writing score'],bins=5)   
#sns.displot(Newstudentdata['writing score'],bins=20)   
#plt.show()
"""
#BoxPlot

sns.catplot(x='math score', kind='box', data= Newstudentdata)
plt.show()


