import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = pd.read_csv(r"D:\data-analytics\Social_Network_Ads.csv")

# Drop unnecessary columns
data.drop(columns=["User ID", "Gender", "EstimatedSalary"], inplace=True)
print(data.head(5))  # Display the first 5 rows of the dataset

# Visualize the relationship between Age and Purchased
sns.scatterplot(x="Age", y="Purchased", data=data)
plt.title("Scatter plot of Age vs Purchased")
plt.show()

# Separate the features and the target variable
x = data.iloc[:, :-1]  # Features (Age)
y = data["Purchased"]  # Target (Purchased)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)  # Data split into training and testing sets

# Display the training set
print(x_train)

# Initialize the Logistic Regression model
lr = LogisticRegression()

# Fit the model to the training data
lr.fit(x_train, y_train)

# Evaluate the model's performance
accuracy = lr.score(x_test, y_test)
print(f"Logistic Regression Accuracy: {accuracy:.2f}")

# Predict the purchase probability for a given age (e.g., 40)
prediction = lr.predict([[40]])
print(f"Prediction for Age 40: {prediction}")

# Visualize the prediction line
sns.scatterplot(x="Age", y="Purchased", data=data)
# sns.lineplot(x="Age", y=lr.predict(x), color="red")  # This is our prediction line
# plt.title("Scatter plot of Age vs Purchased with Prediction Line")
# plt.show()


#WITH MULTIPLE INPUTS PREDICTIONS


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data2 = pd.read_csv("D:\data-analytics\Social_Network_Ads.csv")
data2.drop(columns=["User ID","Gender"], inplace = True)
data2.head(5)


sns.scatterplot(x="Age",y="EstimatedSalary", data=data2, hue="Purchased")

x = data2.iloc[:,:-1]
y = data2["Purchased"]


x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,y_train)

lr.score(x_test,y_test)

lr.predict([[48,41000]])

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.to_numpy(), y.to_numpy(), clf=lr)
plt.show()

lr.intercept_
lr.coef_



#LOGICTIC REGRESSION USING POLYNOMIAL FEATURES

from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2) #hum degrees ki value badhate jayenge toh humme accuracy me variation dekhne milne lagega, jis degree me accuracy high milegi ussko hi consider krenge 
pf.fit(x)
x = pd.DataFrame(pf.transform(x))
x

x_train, x_test , y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
from sklearn.linear_model import LogisticRegression 
lr = LogisticRegression()
lr.fit(x_train,y_train)

lr.score(x_test,y_test) #issme toh aur jyda kam hogya hmari accuracy 
#degree bada rahe hai to accuracy aur kam hoti ja rhi hai

#issliye hum yahn pr linear logisctic regression ko follow krenge
#y = 1/(1+e^-x)


#LOGISTIC REGREESSION IN MULTICLASS - CLASSIFICATION


dataset = pd.read_csv("D:\data-analytics\Iris.csv")
dataset.head(5)
dataset["Species"].unique()

sns.pairplot(data=dataset, hue = "Species")

#in saare graph se hme features selectionn krne ki knowledge mil skti hai
x = dataset.iloc[:,:-1]
y = dataset["Species"]

x_train1, x_test1 , y_train1, y_test1 = train_test_split(x,y,test_size=0.2, random_state=42)
from sklearn.linear_model import LogisticRegression 

#ovr method
lr2 = LogisticRegression(multi_class="ovr")
lr2.fit(x_train1,y_train1)
lr2.score(x_test1,y_test1)*100 #100% accuracy using ovr method

#multinomial

lr3 = LogisticRegression(multi_class="multinomial")
lr3.fit(x_train1,y_train1)
lr3.score(x_test1,y_test1)*100 #100% accuracy using ovr method


#auto
lr4 = LogisticRegression(multi_class="auto")
# lr4 = LogisticRegression() => hum aisa bhi use kr skte hai, yhan pr bhi yeh auto hi hoga aur same result aayega
lr4.fit(x_train1,y_train1)
lr4.score(x_test1,y_test1)*100 #100% accuracy using ovr method