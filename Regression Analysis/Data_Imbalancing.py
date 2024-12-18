import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("D:\data-analytics\Social_Network_Ads.csv")
data.head(5)

data.drop(columns=["User ID","Gender"], inplace = True)

x = data.iloc[:,:-1]
y = data["Purchased"]

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
y_train

data["Purchased"].value_counts()
# 0 -> 257 and 1 -> 143 yaani data me imbalancing hai issliye jab bhi hum iss data me hum modelko train krenge toh woh 0 ke taraf biased ho jayega , issko dooor krne ke liye hum use krenge imbalancing technique ka

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,y_train)

lr.score(x_test , y_test)
lr.predict([[46, 28000]]) #yeh most of the cases me 0 hi de rha hai bhale isska answer 1 h tb bhii, kyuki issme data imbalancing hai


#random undder sampling

#undersampling me data me jo bda hai woh kam wale ke barabar ho jayega!
#kam -> 150 , jyda -> 500 toh , kam-150, jyda->150

from imblearn.under_sampling import RandomUnderSampler
ru = RandomUnderSampler()
ru.fit(x,y)

ru_x , ru_y = ru.fit_resample(x,y)
ru_y 
ru_y.value_counts()

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(ru_x, ru_y, test_size=0.2, random_state=42)
y_train

from sklearn.linear_model import LogisticRegression
lr1 = LogisticRegression()

lr1.fit(x_train,y_train)
lr1.score(x_test , y_test)

lr1.predict([[17, 25000]])

#Random Over Sampling

#oversampling me data me jo kam hai woh bade wale ke barabar ho jayega! yani kam wala jyda ho jayega
#kam -> 150 , jyda -> 500 toh , kam-500, jyda->500


from imblearn.over_sampling import RandomOverSampler
ro = RandomOverSampler()
ro.fit(x,y)

ro_x , ro_y = ro.fit_resample(x,y)
ro_y 

ro_y.value_counts()

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(ro_x, ro_y, test_size=0.2, random_state=42)
y_train

from sklearn.linear_model import LogisticRegression
lr2 = LogisticRegression()

lr2.fit(x_train,y_train)
lr2.score(x_test , y_test)

lr2.predict([[17, 25000]])