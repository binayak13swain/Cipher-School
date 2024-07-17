# -*- coding: utf-8 -*-
"""Lecture 16 - Working With Data Using Pandas

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gc4m5jnQIPk1uumy6z-1UDoccJtKKQ7C
"""

import pandas as pd

#Creating a DataFrame from a dictionary
data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35],
    'City' : ['New York' , 'Los Angles' , 'Chicago']
}

df = pd.DataFrame(data)
print(df)

"""# Creating a dataframe from a list of dictionaries"""

data = [
    {'Name':'Alice', 'Age': 25, 'City' : 'New York'},
    {'Name':'Bob', 'Age': 30, 'City' : 'Los Angles'},
    {'Name':'Charlie', 'Age': 35, 'City' : 'Chicago'}
]

df = pd.DataFrame(data)
print(df)

"""## Creating a dataframe from a csv file"""

#Assuming 'data.csv' is a CSV file int he current directory

df = pd.read_csv('dataset5.csv')
print(df)
print(df.head()) #top 5 rows
print(df.tail())
print(df.info())
print(df.describe())

"""# Selecting Columns"""

print(df['Name'])
print(df[['Name','City']])

"""# Filtering Columns"""

print(df[df['Age'] > 30])

"""# Add new columns"""

df['Salary'] = [50000, 60000, 70000, 80000]
print(df)

"""# Modifying existing columns"""

df['Age'] = df['Age'] + 1
print(df)

"""# Dropping rows and columns"""

df = df.drop(columns=['Salary'])
print(df)

#dropping a row
df = df.drop(index = 1)
print(df)

"""# Grouping data"""

#Grouping data by column

grouped = df.groupby('City')
print(grouped['Age'].mean())

"""# Aggregating data"""

# Aggregating data using multiple functions
aggregated = df.groupby('City').agg({'Age' : ['mean', 'min', 'max']})
print(aggregated)

"""# Merging dataframes"""

df1 = pd.DataFrame({'ID' : [1, 2, 3], 'Name' : ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID' : [1, 2, 4], 'Salary' : [50000, 60000, 70000]})

# Merging dataframes on a common column
merged_df = pd.merge(df1, df2, on = 'ID', how = 'inner')
print(merged_df)

"""# Joining dataframes

"""

df1 = pd.DataFrame({'Name' : ['Alice','Bob'], 'Age': [25, 30]}, index = [0,1])
df2 = pd.DataFrame({'City' : ['New York', 'Los Angles']}, index=[0, 2])

#Joining dataframes on their index
joined_df = df1.join(df2, how = 'left')
print(joined_df)
