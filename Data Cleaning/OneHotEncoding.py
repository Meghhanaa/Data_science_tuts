# Importing necessary libraries
import pandas as pd               # For data manipulation and analysis
import seaborn as sns             # For data visualization (useful for exploratory data analysis)
import numpy as np                # For numerical computations
import matplotlib.pyplot as plt   # For plotting (if needed)

# Load the dataset into a Pandas DataFrame
data = pd.read_csv(r"D:\data-analytics\loan.csv")  
print("Initial Data Preview:")
# print(data.head())  # Display the first 5 rows of the dataset

# Fill missing values in the 'Gender' column with its mode (most common value)
data["Gender"].fillna(data["Gender"].mode()[0], inplace=True)

# Fill missing values in the 'Married' column with its mode
data["Married"].fillna(data["Married"].mode()[0], inplace=True)

# Extract columns 'Gender' and 'Married' into a new DataFrame
en_data = data[["Gender", "Married"]]
# Apply one-hot encoding to the selected columns and display their information
print(pd.get_dummies(en_data).info())

from sklearn.preprocessing import OneHotEncoder

#one-hot-encoding ke through hum jo bhi upr data bool data type me aaya haii ussko hum , integer type me convert kar skte haii, kyuki normal me(jo ki methods upr use hui hai) ussko use krne se boolean ban jata haii

#fit_transform = fit jo bhi data hum ussko dete hai ussko dekhta hai smjhta hai fr ussme scikit learn ki algorithm ko apply krta hai, fir jo bhi data haii ussko transform kr deta haii aur numerical data me convert kr deta h categorical data ko, jaise ki gender me do hote h male aurr female to ussko dekhega and then ussko transform kr dega , do alag items me

#sparse matrix => yeh woh matrix hoti hai jisme saare contents 0-1 ke form me hote haii

#one hot encoding ke andar saare data , 0/1 ke form me hi rhte haii

# One-hot encoding without dropping any category
ohe = OneHotEncoder()  # Creating an instance of OneHotEncoder
ar = ohe.fit_transform(en_data).toarray()  # Encoding the 'Gender' and 'Married' columns into binary arrays
print("\nOne-Hot Encoded Array:")
print(ar)

# Convert the encoded array into a DataFrame with appropriate column names
encoded_df = pd.DataFrame(ar, columns=["Gender_Female", "Gender_Male", "Married_No", "Married_Yes"])
print("\nOne-Hot Encoded DataFrame without Dropping Any Category:")
print(encoded_df.head())  # Display the first 5 rows of the DataFrame

# One-hot encoding with the 'drop' parameter to avoid multicollinearity
# Drop the first category for each column (e.g., 'Gender_Female', 'Married_No')
ohe2 = OneHotEncoder(drop="first")  
ar2 = ohe2.fit_transform(en_data).toarray()  # Encoding the 'Gender' and 'Married' columns
print("\nOne-Hot Encoded Array with 'Drop First' Option:")
print(ar2)

# Convert the encoded array into a DataFrame with reduced column names
reduced_df = pd.DataFrame(ar2, columns=["Gender_Male", "Married_Yes"])
print("\nOne-Hot Encoded DataFrame with 'Drop First' Option:")
print(reduced_df.head())  # Display the first 5 rows of the DataFrame