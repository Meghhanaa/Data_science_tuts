import numpy as np
import pandas as pd

data = pd.read_csv("D:\owner(2).csv")
print(data)
print(data.isnull())

print(data.isnull().sum())  #gives all the cells into true or false , if cell is null then true else false

print(data.dropna())  #delete all the rows which contains the null values inn any of the cells

print(data["o_aadhar"].mean())  # null values ko ussi ke avg se replace krne se baad me kabhi bhi uss column ka avg nikalenge to frk nahi padega (yeh sab generally un jagh use hota hai jaha values hoti h, string ke case me nahi)

data["o_aadhar"] = data["o_aadhar"].replace(np.nan, 470500000000.0) #replaced the null values with specific values

print(data["o_aadhar"])

print(data["o_aadhar"].mean()) #before and after the mean is same

print(data.fillna(method = 'ffill'))  #forward fill ->  mtlb ki agar koi data me hme null values ko replace krna hai to hum upar wale data ko as it is null me replace kr denge ya fill kr denge

print(data.fillna(method = 'bfill'))  #backward fill -> same as forward fill bss niche wali values ko fill kr dete hai
#ye saare use hote hai thodi bahut data accuracy ke liyee

