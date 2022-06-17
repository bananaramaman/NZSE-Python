#Lab6 Predicitve Data Analysis

from turtle import pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

houseData = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab6_PredictiveAnalysisUsingPython\Lab6_kc_house_data.csv")
print(houseData.head(5))

#Data Exploration

print(houseData.shape)
print(houseData.describe())

#Data Cleaning 

print(houseData.isnull().sum())
print(houseData.nunique())

#Data Visualisation
"""
#Histogram
bedrooms=houseData["bedrooms"]
plt.hist(bedrooms, bins=33)
plt.show()

bedrooms= houseData["bedrooms"]
plt.hist(bedrooms)
plt.show()

bathrooms=houseData["bathrooms"]
plt.hist(bathrooms)
plt.show()
"""
#Our main aim is to predict the price of a house. so for this we will need to train and later test the data,
#But deofre that we need to see the relationship of the price of the house with parameters like bedroom, bathroom
#sqft living, lot area, etc.
"""
#sns.relplot(x='price', y="bedrooms", data=houseData)
#plt.show()
#sns.relplot(x='price', y='bathrooms', data=houseData)
#plt.show()

#sns.relplot(x='price', y='sqft_living', data=houseData)
#plt.show()

#sns.relplot(x='price', y='sqft_lot', data=houseData)
#plt.show()

#sns.relplot(x='price', y='waterfront', data=houseData)
#plt.show()

#sns.relplot(x='price', y='sqft_living',hue="waterfront",data=houseData)
#plt.show()
"""
#Modelling 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#train= houseData.drop(['price', 'id', 'date', 'lat', 'long','zipcode','yr_built','yr_renovated'], axis=1)
train= houseData.drop(['price', 'id', 'date'], axis=1)
test=houseData['price']

#Using train test method
X_train,X_test,Y_train,Y_test = train_test_split(train,test,test_size=0.2,random_state=2)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

#Model Creation 
regr=LinearRegression()

regr.fit(X_train, Y_train)
pred=regr.predict((X_test))
print(pred[0:5])

#Plotting the prediction against the Y_Test
"""
plt.scatter(Y_test, pred)
plt.xlabel("TRUE VALUES")
plt.ylabel("PREDICTED VALUES")
plt.show()
"""
#Checking how good our prediction is.
print(regr.score(X_test,Y_test))
