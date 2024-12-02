import pandas as pd

data = {"name": ["megh" , "deeksha" , "rani"], "age": [28,23,30], "salary" :[3000,4000,5000]}

df = pd.DataFrame(data)
# print(df)

df2 = pd.read_csv("D:\customer(1).csv")
print(df2)
print(df2.head(5))   #starting se 5 values
print(df2.tail(5))   # ending se 5 values
print(df2.info)
print(df2.describe)
print(df2.isnull().sum())