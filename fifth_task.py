import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("C:\\Users\\mayan\\Downloads\\heart.csv")

# Set a style
sns.set_style("whitegrid")

# Q1: Distribution of age among patients
plt.figure(figsize=(12, 6))
sns.histplot(df['age'], bins=30, kde=True, color='dodgerblue')
plt.title('Distribution of Age', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Q2: Distribution of cholesterol levels by sex
plt.figure(figsize=(12, 6))
sns.boxplot(x='sex', y='chol', data=df)
plt.title('Cholesterol Levels by Sex', fontsize=16)
plt.xlabel('Sex (0 = Female, 1 = Male)', fontsize=14)
plt.ylabel('Cholesterol', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Q3: Correlation between different features
plt.figure(figsize=(14, 10))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix', fontsize=16)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.show()

# Q4: Average maximum heart rate achieved by patients grouped by target
plt.figure(figsize=(12, 6))
thalach_mean = df.groupby('target')['thalach'].mean().reset_index()
sns.barplot(x='target', y='thalach', data=thalach_mean)
plt.title('Average Maximum Heart Rate by Heart Disease Presence', fontsize=16)
plt.xlabel('Heart Disease (0 = No, 1 = Yes)', fontsize=14)
plt.ylabel('Average Maximum Heart Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Q5: Fasting blood sugar levels
plt.figure(figsize=(12, 6))
fbs_counts = df['fbs'].value_counts().reset_index()
fbs_counts.columns = ['FBS Level', 'Count']  # Rename columns for clarity
sns.barplot(x='FBS Level', y='Count', data=fbs_counts)
plt.title('Fasting Blood Sugar Levels', fontsize=16)
plt.xlabel('Fasting Blood Sugar (0 = <= 120 mg/dl, 1 = > 120 mg/dl)', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Q6: Distribution of chest pain types
plt.figure(figsize=(12, 6))
cp_counts = df['cp'].value_counts().reset_index()
cp_counts.columns = ['Chest Pain Type', 'Count']  # Rename columns for clarity
sns.barplot(x='Chest Pain Type', y='Count', data=cp_counts)
plt.title('Chest Pain Types', fontsize=16)
plt.xlabel('Chest Pain Type', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Q7: Relationship between age and maximum heart rate achieved
plt.figure(figsize=(12, 6))
sns.scatterplot(x='age', y='thalach', data=df, hue='target', s=100)
plt.title('Age vs. Maximum Heart Rate Achieved', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Maximum Heart Rate Achieved', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Heart Disease', fontsize=12, title_fontsize=14)
plt.show()

# Q8: Heart disease presence
plt.figure(figsize=(12, 6))
target_counts = df['target'].value_counts().reset_index()
target_counts.columns = ['Heart Disease', 'Count']  # Rename columns for clarity
sns.barplot(x='Heart Disease', y='Count', data=target_counts)
plt.title('Heart Disease Presence', fontsize=16)
plt.xlabel('Heart Disease (0 = No, 1 = Yes)', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
