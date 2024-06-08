import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the dataset
data = pd.read_csv('C:\\Users\\mayan\\Downloads\\usvid.csv')
print(data.head())  # Shows the top 5 rows

# Print the dimensions of the data before removing the duplicates
print("Data size before removing duplicates:", data.shape)

# Remove duplicate rows from the DataFrame
data.drop_duplicates(inplace=True)

# Print the dimensions of the DataFrame after removing duplicates
print("Data size after removing duplicates:", data.shape)

# Removing the Columns which are not essential
redundant_columns = ["thumbnail_link", "description"]
data.drop(redundant_columns, axis=1, inplace=True)
print(data.info())

# Assuming df is your DataFrame and trending_date is in the format 'yy.mm.dd'
data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')

print("Displaying data after correcting the date format")
print(data.head(3))

# Process publish time
data['publish_time'] = pd.to_datetime(data["publish_time"])
print(data.head(2))

# Adding new columns
data["publish_day"] = data["publish_time"].dt.day
data["publish_month"] = data["publish_time"].dt.month
data["publish_year"] = data["publish_time"].dt.year

# Counting the total videos in year
yearly_counts = data.groupby("publish_year").count()

print(sorted(data["category_id"].unique()))

data['category_name'] = np.nan
data.loc[(data["category_id"] == 1), "category_name"] = 'Film and Animation'
data.loc[(data["category_id"] == 2), "category_name"] = 'Autos and Vehicles'
data.loc[(data["category_id"] == 10), "category_name"] = 'Music'
data.loc[(data["category_id"] == 15), "category_name"] = 'Pets and Animals'
data.loc[(data["category_id"] == 17), "category_name"] = 'Sports'
data.loc[(data["category_id"] == 19), "category_name"] = 'Travel and Events'
data.loc[(data["category_id"] == 20), "category_name"] = 'Gaming'
data.loc[(data["category_id"] == 22), "category_name"] = 'People and Blogs'
data.loc[(data["category_id"] == 23), "category_name"] = 'Comedy'
data.loc[(data["category_id"] == 24), "category_name"] = 'Entertainment'
data.loc[(data["category_id"] == 25), "category_name"] = 'News and Politics'
data.loc[(data["category_id"] == 26), "category_name"] = 'How to and Style'
data.loc[(data["category_id"] == 27), "category_name"] = 'Education'
data.loc[(data["category_id"] == 28), "category_name"] = 'Science and Technology'
data.loc[(data["category_id"] == 29), "category_name"] = 'Non Profits and Activism'
data.loc[(data["category_id"] == 30), "category_name"] = 'Movies'
data.loc[(data["category_id"] == 43), "category_name"] = 'Shows'

print(data.head())

# Plotting views for top 5 categories
yearly_views = data.groupby("publish_year")['views'].sum().reset_index()

# Creating the bar chart
yearly_counts.plot(kind='bar', color='skyblue', edgecolor='black', xlabel='Year', ylabel='Total Publish Count', title='Total Publish Video Per Year', figsize=(10, 6), grid=True).set_facecolor('#f0f0f0')
plt.show()

# Group by year and sum the views for each year
yearly_views = data.groupby('publish_year')['views'].sum()

# Create a bar chart
yearly_views.plot(kind='bar', xlabel='Year', ylabel='Total views', title='Total Views per year')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Group the data by 'category_name' and calculate the sum of 'views' in each category
category_views = data.groupby('category_name')['views'].sum().reset_index()

# Sort the categories by views in descending order
top_categories = category_views.sort_values(by='views', ascending=False).head(5)

# Creating a bar plot to visualize the top 5 categories
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)
plt.title('Top 5 Categories', fontsize=15)
plt.tight_layout()
plt.show()

# Creating bar chart for video count by category
plt.figure(figsize=(12, 6))
sns.countplot(x='category_name', data=data, order=data['category_name'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Video Count by Category')
plt.show()

# Count the number of videos published per hour
data['publish_hour'] = data['publish_time'].dt.hour
videos_per_hour = data['publish_hour'].value_counts().sort_index()


# Create a bar plot for Number of Videos Published per Hour
plt.figure(figsize=(12, 6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')
plt.title('Number of Videos Published per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()

# Creating a line plot for Videos Published Over Time
data['publish_date'] = data['publish_time'].dt.date
video_count_by_date = data.groupby('publish_date').size()
plt.figure(figsize=(12, 6))
sns.lineplot(data=video_count_by_date)
plt.title("Videos Published Over Time")
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=90)
plt.show()

# Scatter plot between views and likes
sns.scatterplot(data=data, x='views', y='likes')
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

# Creating multiple subplots for different counts
plt.figure(figsize=(14, 8))
plt.subplots_adjust(wspace=0.5, hspace=0.8, top=0.9)

plt.subplot(2, 2, 1)
g = sns.countplot(x='comments_disabled', data=data)
g.set_title("Comments Disabled", fontsize=16)

plt.subplot(2, 2, 2)
g1 = sns.countplot(x='ratings_disabled', data=data)
g1.set_title("Rating Disabled", fontsize=16)

plt.subplot(2, 2, 3)
g2 = sns.countplot(x='video_error_or_removed', data=data)
g2.set_title("Video Error or Removed", fontsize=16)

plt.show()

# Finding the correlation
corr_matrix = data['views'].corr(data['likes'])
print("Correlation between views and likes:", corr_matrix)
