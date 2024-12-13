# Simple linear regression me ek input hoga aur ek hi output hoga, yaani ek input se hi hme output predict krna hai

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the specified path
data = pd.read_csv("D:\\data-analytics\\placement.csv")
data.head(5)  # Display the first 5 rows of the dataset

# Plot a scatterplot to visualize the relationship between CGPA and package
sns.scatterplot(x="cgpa", y="package", data=data)

# Check for any missing values in the dataset
data.isnull().sum()

# y -> dependent , x -> independent (y = mx+c)
# x ke basis pe hum y ko nikalenge,
x = data[["cgpa"]]  # Extract the independent variable (feature)
y = data["package"]  # Extract the dependent variable (target)
x.ndim, y.ndim  # Check the dimensions of x and y

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) #agar random_state nahi use krenge toh kya hoga? Agar random_state use nahi karte hain toh har baar jab aap code ko run karenge, data randomly split hoga. Iska matlab hai ki training aur testing sets har run me alag-alag honge, jo ki kuch situations me problem create kar sakta hai

# issme data ko do part me divide kr diya hai randomly , train krne ke liye aur test krne ke liye
x_train  # Display the training data for x

from sklearn.linear_model import LinearRegression

lr = LinearRegression()  # Initialize the Linear Regression model
# linear equation -> y=mx+c
# linear regression kya krta hai ek line deta hai jo ki input data se bicho bich hokr guzre, jisse ki hum unknown quantity jaise ki m and c find out kr paye aur next time new input data me sahi se work kare,

lr.fit(x_train, y_train)  # Fit the model to the training data

# Predict the package for a given CGPA value
lr.predict([[7.42]])  # yhan pr yeh linear regression ka predict method hai jo ki train data ke base pe trained ho chuka hai and hum kisi bhi value ko deke test kr skte hai ki jo bhi cgpa denge ussko as paas ki value de de ussko, agar de rha hai to sahi se trained hua hai

# Evaluate the model's performance
lr.score(x_test, y_test)  # yeh function btata hai ki hmara answer kitne % accurate hai

lr.coef_ , lr.intercept_ #y = mx+c , m = coef and c = intercept

y = 0.57425647 * x -1.0270069374542108 #yeh hmari equation nikal ke aaayi hai, ab hum cross check kr lete hai values rkh ke
0.57425647 * 7.42 -1.0270069374542108 #exact same value aayi hai upr se

y_prd = lr.predict(x) #yehi variabe hum user ya client ko dete hai , yani ab hmara model trained ho chuka hai issko hum paas on kr skte hai,
sns.scatterplot(x="cgpa",y="package",data=data)
# plt.plot(x,y) #yeh normally ban gaya hai, 
plt.plot(data["cgpa"], y_prd, color = "red")
plt.legend(["original data","predicted line"])
plt.savefig("predict.jpg") #yeh graph as a jpg format me hmare system me save ho jayegiiii
plt.show()


#hume yehi kosish krna hai ki jyda se jyda accuracy aaye, kyuki jitni jyda accuracy utna achhha hmara answer predict hokr aayega,