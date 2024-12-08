# Importing necessary libraries
import pandas as pd               # For data manipulation and analysis
import seaborn as sns             # For data visualization (useful for exploratory data analysis)
import numpy as np                # For numerical computations
import matplotlib.pyplot as plt   # For plotting (if needed)

# Load the dataset into a Pandas DataFrame
data = pd.read_csv(r"D:\data-analytics\loan.csv")  
print("Initial Data Preview:")
# print(data.head())  # Display the first 5 rows of the dataset

# Extract column names of float64 data types
cols = data.select_dtypes(include=['float64']).columns.values
print("\nColumns with float64 data type:")
print(cols)

# Importing SimpleImputer to handle missing values
from sklearn.impute import SimpleImputer

# Create an imputer object to replace missing values with the mean
si = SimpleImputer(strategy="mean")

# Apply the imputer to the selected float columns and transform the data
ar = si.fit_transform(data[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']])

# Convert the transformed array back to a DataFrame with original column names
new_data = pd.DataFrame(ar, columns=data.select_dtypes(include=['float64']).columns.values) #mean hum issliye daaal rhe h kyuki overall data me koi frk nahi pdega kuch bhi niklege tohh

print("\nNew DataFrame after handling missing values:")
print(new_data.head())  # Display the first 5 rows of the cleaned DataFrame

# Check for any remaining missing values
missing_values = new_data.isnull().sum()
print("\nMissing values in new DataFrame (should be zero):")
print(missing_values)

# Calculate the mean of the 'LoanAmount' column in the cleaned data
mean = np.mean(new_data["LoanAmount"]) #check krne ke liye ki jo mean table me fill hua hai wohi hai ki nahi
print("\nMean Loan Amount after cleaning:")
print(mean)
