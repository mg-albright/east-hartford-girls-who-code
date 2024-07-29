import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Introduction to Lists
# ======================

# Creating a list of integers
numbers = [1, 2, 3, 4, 5]
print("List of Numbers:", numbers)

# Accessing elements in a list
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Modifying elements in a list
numbers[2] = 10
print("Modified List:", numbers)

# Adding elements to a list
numbers.append(6)
print("List after Append:", numbers)

# Removing elements from a list
numbers.pop(2)
print("List after Pop:", numbers)

# Introduction to Pandas DataFrames
# =================================

# Creating a DataFrame from a list of dictionaries
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("\nDataFrame:")
print(df)

# Accessing columns in a DataFrame
print("\nColumn 'Name':")
print(df['Name'])

# Accessing rows in a DataFrame
print("\nRow 1:")
print(df.loc[0])

# Adding a new column to the DataFrame
df['Occupation'] = ['Engineer', 'Designer', 'Student', 'Manager']
print("\nDataFrame with Occupation:")
print(df)

# Removing a column from the DataFrame
df.drop('City', axis=1, inplace=True)
print("\nDataFrame after removing 'City' column:")
print(df)


# First Plotting example:
# ========================

# # Generate random data for demonstration
# categories = ['Category A', 'Category B', 'Category C', 'Category D']
# values = np.random.randint(1, 10, size=len(categories))

# # Plotting the bar chart
# plt.bar(categories, values, color='skyblue')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Data Visualization Example')

# # Display the plot
# plt.show()


# Second Plotting example:
# =========================

# # Generate or load data
# # For demonstration, we'll create a DataFrame with random data
# data = {
#     'Category': ['A', 'B', 'C', 'D'],
#     'Values': np.random.randint(1, 10, size=4),
#     'Percentage': np.random.rand(4) * 100
# }
# df = pd.DataFrame(data)

# # Bar chart
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 3, 1)
# plt.bar(df['Category'], df['Values'], color='skyblue')
# plt.title('Bar Chart')
# plt.xlabel('Categories')
# plt.ylabel('Values')

# # Pie chart
# plt.subplot(1, 3, 2)
# plt.pie(df['Percentage'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue', 'lightpink'])
# plt.title('Pie Chart')

# # Line plot
# plt.subplot(1, 3, 3)
# x_values = np.linspace(1, 10, num=10)
# y_values = np.random.randint(1, 10, size=10)
# plt.plot(x_values, y_values, marker='o', linestyle='-', color='orange')
# plt.title('Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # Adjust layout to prevent overlapping
# plt.tight_layout()

# # Display the plots
# plt.show()
