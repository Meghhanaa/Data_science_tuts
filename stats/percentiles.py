import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("/data-analytics/titanic.csv")
# print(data.head)

# print(data.isnull().sum())
data["Age"].fillna(data["Age"].mean(), inplace=True)
# print(data["Age"])

p25 = np.percentile(data["Age"],25)
p75 = np.percentile(data["Age"],75)
p0 = np.percentile(data["Age"],0)
print(p25,p75,p0)
print(data["Age"].max())
print(data["Age"].min()) #similar as the 0th percentiles

#75% data 35 tk me hi khtm ho jarha haii lekin max  value 80 tk gayi hai (kaafi bada gap hai) isska mtlb hai ki outliers present hai iss pure data me
# min = 0.42 yani 4 mahine ka age , then 25% = 22 years toh gap hai yaanii outliers hai , jitna kam gap hoga utna kam outliers present honge

# sns.boxplot(x="Age", data=data)
# plt.show()

sns.boxplot(x="Fare", data=data)
plt.show() #issme max aur 75% me gap jyda hai issliye yeh outliers max side hai issliye graph usske according bana haii