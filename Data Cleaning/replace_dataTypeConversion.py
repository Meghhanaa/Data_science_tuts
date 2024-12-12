import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"D:\data-analytics\loan.csv")
data

data.describe()
data.isnull().sum()
data["Dependents"].value_counts() #isse 3+ values hai jo ki ek string type hai issliye yeh dependents ka overall data type object ka kr deta hai 

data["Dependents"].fillna(data["Dependents"].mode()[0], inplace = True)
data["Dependents"].replace("3+","3", inplace = True)#object data type se int krne ke liye phle hume 3+ ko hata ke 3 krne pdega, nahi to error dega, 
data

data["Dependents"] = data["Dependents"].astype("int64") #then object data type ko int64 me convert kr diya gaya
data.info() #yahan se hum wps check kr skte hai