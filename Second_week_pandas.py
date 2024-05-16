import pandas as pd
data = pd.read_csv('01.Data Cleaning and Preprocessing (1).csv')
#printing the initial and bottom five rows

print(data.head(5),data.tail(5))

#printing the data information
print("printing the data information")
print(data.info())

#printing the count of null values
print("Total numbersof null values in particular columns")
print(data.isnull().sum())
print("\n")
print("Total count of null values in the whole given dataset:",data.isnull().sum().sum())
print("\n Data after dropping duplicate values")
data.drop_duplicates(inplace=True)
print(data)

#Filling the NULL values using before and forward fill methods
print("\n Using Before Fill Method:")
print (data.fillna(method="bfill"))

print("\n Using Forward Fill Method:")
print (data.fillna(method="ffill"))

#Filling the NULL values  by Customised value
data.fillna(value=0,inplace=True)
print(data)

#Using basic statics on Dataset
"""Removing the unnecessary columns"""
print("\n Removing the unnecessary columns:")
data.drop(columns="Observation",inplace=True)
print (data)

#Calculating stats upon dataset

print("\n Calculating stats upon the given dataset:")
print (data.describe())


