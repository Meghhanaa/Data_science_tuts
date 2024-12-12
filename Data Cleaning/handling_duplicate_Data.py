import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Creating a sample DataFrame
d = {"name":["a","b","c","d","a","c"], "eng":[8,7,5,8,8,5],"hindi":[2,3,4,5,2,6]}
df = pd.DataFrame(d)
print(df)

# Adding a column to indicate duplicates
df["dup"] = df.duplicated()
print(df)

# Dropping duplicates, only keeping the first occurrence
df.drop_duplicates(inplace=True)
print(df)

# Loading data from a CSV file
data = pd.read_csv(r"D:\data-analytics\loan.csv")
print(data)

# Generating descriptive statistics
print(data.describe())

# Counting the number of duplicate rows
print(data.duplicated().sum())

# Checking the shape of the DataFrame
print(data.shape)

# Dropping duplicates (Note: The result is not saved in a new variable)
data.drop_duplicates(inplace=True)
print(data.shape)  # To verify the shape after dropping duplicates
