import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the specified path
data2 = pd.read_csv("D:\\data-analytics\\multiple_linear_regression_dataset.csv")
data2.head(5)  # Display the first 5 rows of the dataset

# Check for any missing values in the dataset
data2.isnull().sum()
data2.shape  # Check the shape (dimensions) of the dataset

data2.ndim  # Data already 2 dimensional hai issliye ab hum issko directly paas kr denge

# Plot scatterplots to visualize the relationship between age and income, and experience and income
plt.subplot(1, 2, 1)
sns.scatterplot(x="age", y="income", data=data2)
plt.subplot(1, 2, 2)
sns.scatterplot(x="experience", y="income", data=data2)

# Create pairplot to visualize relationships between all numeric variables
sns.pairplot(data=data2)

# Create a heatmap to visualize correlations between variables
sns.heatmap(data=data2.corr(), annot=True)

# Extract independent variables (features) and dependent variable (target)
x = data2.iloc[:, :-1]
y = data2["income"]

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()  # Initialize the Linear Regression model
lr.fit(x_train, y_train)  # Fit the model to the training data

# Evaluate the model's performance
lr.score(x_test, y_test)
lr.coef_, lr.intercept_

# Predict the income for a given age and experience
lr.predict([[43, 10]])  # this is the predicted value, whenever we paas the age and the experice then upto 93% of the accuracy the value will get predicted

# yeh jo equation niche hai given yahi hmari algorithm hai, jiska use krke hum data ki value predict krenge
# y = m1x1 + m2x2 + c => y = -101.0592335 * age + 2154.80549277 * experience + 31465.056418503944  lets verify using this formula
-101.0592335 * 43 + 2154.80549277 * 10 + 31465.056418503944 
# the same exact value is predicted successfully
