import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"D:\data-analytics\loan.csv")
data

data.describe()

#STANDARDIZATION

data.isnull().sum()
sns.distplot(data["ApplicantIncome"])
data.describe() #yhan pr hum dekh skte hai ki ApplicantIncome me min and max value me bahut difference hai issko hi remove krne ke liye hum feature scaling ka use krenge, 

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
data["ss_ApplicantIncome"] = ss.fit_transform(data[["ApplicantIncome"]])
#jab single square brakets use krte hai tb , output as a pandas series return hota hai
#jab double brakets lagate hai tb, op as a dataframe return hota hai

data.head(5)
data.describe()

# Plotting the distributions 
plt.figure(figsize=(12, 5)) 
# Before scaling 
plt.subplot(1, 2, 1) 
plt.title("Before scaling") 
sns.distplot(data["ApplicantIncome"], kde=True) 

# After scaling 
plt.subplot(1, 2, 2) 
plt.title("After scaling") 
sns.distplot(data["ss_ApplicantIncome"], kde=True)
plt.show()


#NORMALIZATION

#Normalization ke andr hum CoapplicantIncome Me work krenge
data.describe()
sns.distplot(data["CoapplicantIncome"])

from sklearn.preprocessing import MinMaxScaler
ss = MinMaxScaler()
data["mm_CoapplicantIncome"] = ss.fit_transform(data[["CoapplicantIncome"]])

data.head(5)
#yhan pahle data 0 to 40000 tak faila tha lekin after scaling 0 to 1 ki range me aagyaa 

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("before scaling")
sns.distplot(data["CoapplicantIncome"])

plt.subplot(1,2,2)
plt.title("After scaling")
sns.distplot(data["mm_CoapplicantIncome"])

plt.show()



