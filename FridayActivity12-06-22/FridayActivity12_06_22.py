from hashlib import new
from turtle import pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#importing data & reading data
propertydata = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\FridayActivity_22-06-12\PapatoetoeProperties1-1.csv")
print(propertydata.head(5))

#Data Exploration

print(propertydata.columns)
print("\n")
print(propertydata.shape)    #(Rows, Columns)
print("\n")
print(propertydata.describe())
print("\n")
#print(propertydata.isnull()) #indicates the null values 
#print(propertydata.isnull().sum()) #Gives a sum of all null values
#print(propertydata.nunique())    #prints the number of unique values
#print(propertydata['Land_Area_mtsq'].unique())      #list the individual unique values


#Data Cleaning

NewPropertyData=propertydata.drop(['Year_Sold','Sold_Month','SNo.','Bedrooms'], axis=1)  #removes the following columns from the data table axis=1 defines the axis to remove from
print(NewPropertyData)


#Relationship Analysis

correlation= NewPropertyData.corr()
#sns.heatmap(correlation, xticklabels=correlation.columns,yticklabels=correlation.columns,annot= True)   #defines the layout of heatmap graph, (annot=True, sets annotations to TRUE)
#plt.show()

#Pairplot

#sns.pairplot(NewPropertyData)
#plt.show()

#Scatterplot

sns.relplot(x="Price_K_NZD",y='Land_Area_mtsq',data=NewPropertyData)
plt.show()


#Histogram plot

sns.distplot(NewPropertyData['CV_K_NZD'])
plt.show()
#sns.distplot(Newstudentdata['writing score'],bins=5)   
#sns.displot(Newstudentdata['writing score'],bins=20)   
#plt.show()

#BoxPlot

sns.catplot(x='CV_K_NZD', kind='box', data= NewPropertyData)
plt.show()
