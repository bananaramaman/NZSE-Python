#Class Activity Fish Exploratory data analysis, Predictive data analysis 

from turtle import pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

fishData = pd.read_csv(r"C:\Users\DJBur\OneDrive - New Zealand Skills & Education Group\SWD503 - Data Analysis\Lab8_Fish\Fish.csv")
print(fishData.head(5))

#Data Exploration

print(fishData.shape)
print(fishData.describe())

#Data Cleaning 

print("\n")
#print(fishData.isnull().sum())
print(fishData.nunique())

#Plotting
sns.relplot(x='Weight', y="Length3",hue="Species",data=fishData)
plt.show()

#sns.relplot(x='Weight', y='Height', data=fishData)
#plt.show()

#sns.relplot(x='Weight', y='Width', data=fishData)
#plt.show()

#sns.relplot(x='Length1',y='Length3',hue="Species", data=fishData)
#plt.show()



#Modelling 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

train= fishData.drop(['Weight','Species'], axis=1)
#train= fishData
test=fishData['Weight']

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

plt.scatter(Y_test, pred)
plt.xlabel("TRUE VALUES")
plt.ylabel("PREDICTED VALUES")
plt.show()

#Checking how good our prediction is.
print(regr.score(X_test,Y_test))