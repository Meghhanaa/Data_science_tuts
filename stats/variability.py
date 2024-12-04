import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# #1. RANGE

# # data = pd.read_csv("/data-analytics/titanic.csv")
# # print(data.head(3))

# # #titanic jahaj ke andr konse age group ke log travel kr rhe the mostlyy

# # minr = data["Age"].min() #minimum age 4 mahine
# # maxr = data["Age"].max() #minimum age 80 years
# # range = maxr - minr
# # print(range) #range hume info deta hai ki konse age griup ke log ussme travel kr rhee haii

# data2 = pd.read_csv("/data-analytics/tips.csv")
# print(data2.head(3))

# minr1 = data2["total_bill"].min() #minimum total_bill 3$ mahine
# maxr1 = data2["total_bill"].max() #minimum total_bill 50$ years
# range2 = maxr1 - minr1 #konsi range me most of the bills ban rhe haii

# print(minr1, maxr1,range2)

#MAD - MEAN ABS DEVIATION

#jaha pr mean same ho do datasets me aur hume kisi ek data set ko choose krna hai to hum kaise karenge, hum mostly woh data ko choose krte hai jisme spreadness kam ho, yaani jo bhii data mean ke jyda aas paas hoga ussko hi lena haiii mostly, jisse spreadness kam ho 


A = np.array([75,65,73,68,72,76])
ma = np.mean(A)
B = np.array([90,47,43,96,93,51])
mb = np.mean(B)
print("means of a and b: ")
print(ma,mb)
nop = np.array([1,2,3,4,5,6])

# plt.scatter(A,nop, label = "section A")
# plt.scatter(B,nop, color = "red", label = "section B")
# plt.plot([70,70,70,70,70,70], nop, c = "green", label = "Mean") #yahan par blue waale dots A ke hai jo ke mean ke paas haii, issliye hum inko hi choose krenge lekin har baar graph bana ke dekhne me accuracy nahi aa payegi issliye hum isski jagh MAD ka use karenge
# plt.legend()
# plt.show()

#using the MAD technique

x = np.abs(A-mb)
y = np.abs(B-mb)
mad_A = np.sum(x/len(A))
mad_B = np.sum(y/len(B))
print("mean abs deviation: ")
print(mad_A, mad_B) #mad A ka kam hai compared to B issliye hum A ko choose karenge agar karna pada toh


#standard deviation and variance

#jiska bhi sd and variance kam hoga usssko hi lena haii

sd1 = np.std(A)
sd2 = np.std(B)

v1 = np.var(A)
v2 = np.var(B)

print("standard deviation: ") # A ka sd kam hai
print(sd1, sd2)
print("variance: ") # A ka variance kam hai issko hi choose karenge
print(v1,v2)