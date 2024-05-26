import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data = pd.read_csv('C:\\Users\\mayan\\Downloads\\householdtask.csv')


#Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='year', y='own', data=data, color='blue', edgecolor='k', alpha=0.7)
plt.title("Ownership Over Years", fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Own', fontsize=14)

plt.show()

#Line chart
plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='own', data=data, marker='o', color='green', label='Own')
plt.title("Ownership Trend Over Years", fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Own', fontsize=14)
plt.legend()

plt.show()

#Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='year', y='own', data=data, palette='viridis')
plt.title("Bar Chart of Ownership Over Years", fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Own', fontsize=14)
plt.show()

#Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['income'], bins=20, edgecolor='k', color='orange')
plt.title("Income Distribution", fontsize=16)
plt.xlabel('Income', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.show()
