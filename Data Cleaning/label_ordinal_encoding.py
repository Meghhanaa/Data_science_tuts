# # Import necessary libraries
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# # Create a sample DataFrame with unsequenced data
# df = pd.DataFrame({"name": ["dog", "cat", "cow", "black", "kanha", "ball"]})  
# print("Original DataFrame:")
# print(df)

# # Perform Label Encoding on the 'name' column
# le = LabelEncoder()
# df["en_code"] = le.fit_transform(df["name"])  # Transform categories into numeric labels
# print("\nDataFrame after Label Encoding:")
# print(df)

# # Load the loan dataset
# data = pd.read_csv(r"D:\data-analytics\loan.csv")  # Load the dataset
# print("\nLoaded Loan Data (First 5 Rows):")
# print(data.head())

# # Display unique values in the 'Property_Area' column
# print("\nUnique Property Areas:")
# print(data["Property_Area"].unique())

# # Apply Label Encoding to the 'Property_Area' column
# la = LabelEncoder()
# data["Property_Area_Encoded"] = la.fit_transform(data["Property_Area"])  # Encode categories
# print("\nData after Label Encoding on 'Property_Area':")
# print(data[["Property_Area", "Property_Area_Encoded"]].head())



#ordinal encoding using scikit learning
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Create a sample DataFrame with ordinal categories
df2 = pd.DataFrame({
    "size": ["s", "m", "l","xl", "m","xl", "s", "l","xl"]  # Ensure this matches the intended data
})

# Check the DataFrame columns
print("Columns in df2:", df2.columns)

# Specify the order of categories explicitly
ord_data = [["s", "m", "l","xl"]]  # Ensure the categories match the unique values in the column

# Initialize the OrdinalEncoder with the specified category order
oe = OrdinalEncoder(categories=ord_data)

# Perform ordinal encoding (ensure the column 'size' exists in df2)
df2["size_encoded"] = oe.fit_transform(df2[["size"]])  # Encode the 'size' column
print("Encoded DataFrame:")
print(df2)


#ordinal encoding using the mapping
ord_Data1 = {"s":0,"m":1,"l":2,"xl":3} #hum yahn pr koi bhi random no. de skte haii jo bhi chahiye, bass yaad rkhe rhna haii
df2["size_En_map"]=df2["size"].map(ord_Data1)
print(df2)


