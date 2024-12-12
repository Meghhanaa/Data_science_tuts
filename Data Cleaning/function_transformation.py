#FUNCTION TRANSFORMATION
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"D:\data-analytics\loan.csv")
data

sns.distplot(data["CoapplicantIncome"])

#issko functionally transfrom krne ke liye pahle issme se hume outlier ko remove krna hoga,
q1 = data["CoapplicantIncome"].quantile(0.25)
q3 = data["CoapplicantIncome"].quantile(0.75)
IQR = q3 - q1
minr = q1 - (1.5 * IQR)
maxr = q3 + (1.5 * IQR)
minr,maxr

data = data[data["CoapplicantIncome"]<=maxr]
sns.distplot(data["CoapplicantIncome"])

#iss wale graph me bhi non normal graph ban rha hai issko remove krne ke liye hum func transformtion ka use krenge
from sklearn.preprocessing import FunctionTransformer
ft = FunctionTransformer(func= np.log1p) #hmne logp1 function define kr diya hai jiske base pe 

#log 10 ya log e dono cases me 0 ya negative values ko handle nahi krta or undesired values jaise ki infinite value de skta hai jo hmare data ko inconsistent bana deti hai isslie hum log1p ka use krte hai jisme -> np.long1p(0) =  hota hai aur dusre jagh bhi numerical stability provide krta hai
data["ft_coapplicantincome"] = ft.fit_transform(data[["CoapplicantIncome"]])

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("before Transform")
sns.distplot(data["CoapplicantIncome"])

plt.subplot(1,2,2)
plt.title("After Transform")
sns.distplot(data["ft_coapplicantincome"]) #yhan pr kuch hadd tak normal distribution achieve kr chuke hai jiski help se data transform ho gaya hai

#yeh sab tb ho rha hai jab hmne issme se outliers remove kr diye the


#ab hum ek naya banayenge jisme bina outliers remove kre kaam ho sake, usske liye bina outliers ko remove kre direct function transformation laga dena hai