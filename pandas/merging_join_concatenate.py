import pandas as pd

# Define the first dictionary and create a DataFrame
d = {"emp id": ["e1", "e2", "e3", "e4", "e5", "e6"],
     "names": ["ram", "shyam", "radha", "kanha", "geeta", "bhola"],
     "age": [32, 38, 25, 36, 26, 45]}

# Define the second dictionary and create a DataFrame
d2 = {"emp id": ["e1", "e2", "e3", "e4", "e5", "e6"],
      "salary": [45000, 55000, 85000, 100000, 60000, 90000]}

# Create DataFrames from dictionaries
df1 = pd.DataFrame(d)
df2 = pd.DataFrame(d2)

# Print the individual DataFrames
print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# Merge the DataFrames on the 'emp id' column
merged_df = pd.merge(df1, df2, on="emp id")

# Print the merged DataFrame
print("\nMerged DataFrame:")
print(merged_df)


# created another dataframe , in this some values are not same as df1
d3 = {"emp id": ["e1", "e8", "e3", "e9", "e5", "e6"],
      "salary": [45000, 55000, 85000, 100000, 60000, 90000]}

df3 = pd.DataFrame(d3)
# Merge the DataFrames on the 'emp id' column
merge2 = pd.merge(df1, df3, on="emp id")

# Print the merged DataFrame
print("\nMerged DataFrame 2:") #issme bass jo matched data honge whii bass show karenge unmatched data merge hi nahi honge
print(merge2)

#left join -> left wali puri data aayega aur jo right wale me yani dusre wale me data nahi h wha pe NaN likha hua aa jayegaa(sql wala left join)
print(pd.merge(left=df1,right=df3,on="emp id",how="left"))

print(pd.merge(left=df1,right=df3,on="emp id",how="right")) #sql wala right join

# Perform a cross join
cross_join_df = pd.merge(left=df1, right=df3, how="cross")

# Print the result of the cross join
print("\nCross Join Result:")
print(cross_join_df) 

#A cross join pairs every row in the left DataFrame with every row in the right DataFrame.
#The result size is len(df1) × len(df3).


#concatenate hone ke liye do data frame honi chahiye, same type ki data alag ho skta haiii

d4 = {"emp id": ["e7", "e8", "e9", "e10", "e11", "e12"],
     "names": ["monu", "sonu", "ranu", "kalu", "golu", "bholu"],
     "age": [32, 38, 25, 36, 26, 45]}

df4 = pd.DataFrame(d4)

print(df4)

print(pd.concat([df1,df4])) #indexinf=g bhi concatenate ho jayegii , mtlb ki agarr hmko do similar table ko jodna hai to jud to jayega lekin same indexing me do do values ho jayengii