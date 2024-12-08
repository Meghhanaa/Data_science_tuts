import pandas as pd
from sklearn.svm import SVC

data = pd.read_csv("D:\data-analytics\scikit_Learn\Seed_Data.csv")
# print(data)

print(data.describe)

from sklearn.model_selection import train_test_split

x_train , x_test, y_train, y_test =  train_test_split(x,y,test_size=0.2, random_state=13)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
clf = svm.SVC()
clf.fit(x_train,y_train)