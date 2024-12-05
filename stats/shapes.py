import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#positive

# data = pd.read_csv("/data-analytics/titanic.csv")
# # print(data.head(3))
# sk = data["Age"].skew()
# print(sk) # sk>0 means +ve skewness hai 
# sns.histplot(x="Age", data=data)
# plt.show()

#negative 

# d = np.random.normal(0,100,100)
# df = pd.DataFrame({"x":d})

# sk2 = df["x"].skew()
# print(sk2) # sk<0 means -ve skewness haii

# sns.histplot(x="x", data=df)
# plt.show() #graph ki value bhi -ve side haii

#normal

d3 = [10,20,30,40,50,60,70,80,90,100]
df2 = pd.DataFrame({"x":d3})
sk3 = df2["x"].skew() #skewness 0 haiii
print(sk3) 

sns.histplot(x="x", data=df2)
plt.show()