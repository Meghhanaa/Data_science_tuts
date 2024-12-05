import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("/data-analytics/tips.csv")
# print(data.head(3))
# print(data.info())

print("correlation") #do data ke bich m relation dekhne ke liyee correlation use krte haii
cor = data.select_dtypes(["float64","int64"]).corr() #correlation
print(cor)

print("covariance")
cov = data.select_dtypes(["float64","int64"]).cov() #covariance
print(cov)

sns.heatmap(cor, annot=True) # jo sabse light color hai woh +ve correlation show kr rha hai aur jo sbse dark hai woh 0 corr ko show krr rha haii,
 
plt.show()