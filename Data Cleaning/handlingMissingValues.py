import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\data-analytics\loan.csv")
data.head(4)

data.shape #row X column
data.isnull().sum() #hum total null values find out krr rhe haii, per column
(data.isnull().sum()/data.shape[0])*100 #per row me kitne % null values hai ussko nikaal rhe haii

data.isnull().sum().sum() #overall file me kitnne null values present hai ussko nikaalne ke liye do baar sum use kiya haii

data.shape[0]*data.shape[1] #total values hai jo ki lean.csv me cells haiii

#total values of null value jo ki present hai iss table me / total values
((data.isnull().sum().sum()) / (data.shape[0]*data.shape[1]))*100

sns.heatmap(data.isnull())
plt.show() #jo bhi white value hai woh sho krr rhi hai ki kitni null values present hai iss data me aur jo black part hai woh show kr rha hai not-null values ko


#DROPPING THE MISSING VALUE 
#KYUKI SHYD UNKA USE NAHI HOGA

#YAHAN PAR HAMRE PAAS DO METHODS HAI , agar kisi column me 50% se jyda data missing hai to hum uss column ko hata dete hai.
# aur agar kisi row me kaafi data missing hai to wha pr hm row ko hi drop kr dete hai

data.drop(columns = ["Credit_History"]) # yeh jo hai to data ko temperory basis pr delete kr dega, lekin excel sheet me nahi delete hoga
data.drop(columns = ["Credit_History"], inplace = True) #isse ho jayega


data.dropna(inplace = True) #isse null values containing row delete ho jayegaa

#FILLING THE MISSING CONTENT

#three types of filling are there, 1. backward filling -> jisme pichhe wala data aange aake bharta hai, 2. forward filling -> me aage waala data pichhe aake bhrta h and 3. MOD 

data.info()
data.bfill() #niche wala data upr aagyaa
data.ffill() #upr wala data niche aagyaa agar upr kuch nahi rhega to nahi aayegaa kuchh bhiii Nan hi rhega

data.ffill(axis = 1) #axis = 1 dene k amtlb h ki joo bhi data left wale column me hoga whi current me aa jayega

#mode wala concept me jo bhi item sabse jyda baar repeat hua hai ussko hi hm rkh lenge missing cell me
data.isnull().sum()

x = data["Gender"].mode()[0] #yeh hmne jo value sabse jyda repeat horhi h ussko nikaaal liya haiii mode func ka use krke
data.fillna(x, inplace  = True) # yeh fill kr dega moded value ko

data.isnull().sum() #ab hmne yahan pr check kiya ki gender me null values present hai ya nahii haii , to nahi haii

#agar hme saare rows and coulmns me moded value fill krna hai to hum loop lagayenge

for i in data:
    x = data[i].mode()[0]
    data.fillna(x, inplace  = True)
    
data.isnull().sum() #saare columns ki null values gauab ho gayiii
