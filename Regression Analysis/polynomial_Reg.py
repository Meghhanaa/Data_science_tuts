import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the specified path
data3 = pd.read_csv("D:\\data-analytics\\Position_Salaries.csv")
data3.head(5)  # Display the first 5 rows of the dataset
data3.shape  # Check the shape (dimensions) of the dataset

# Scatter plot to visualize the relationship between Level and Salary
plt.scatter(data3["Level"], data3["Salary"])

# Extract independent variable (Level) and dependent variable (Salary)
x = data3[["Level"]]
y = data3["Salary"]

from sklearn.preprocessing import PolynomialFeatures

# Create Polynomial Features with a degree of 2
pf = PolynomialFeatures(degree=2)  # yeh batata hai ki kitne level ka degree of polynomial hai
pf.fit(x)  # Fit the PolynomialFeatures to the data
x = pf.transform(x)  # Transform the original features to polynomial features

# Equation for the polynomial curve => y = m1x1 + m2x2^2 + c
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)  # issme data ko do part me divide kr diya hai randomly, train krne ke liye aur test krne ke liye

from sklearn.linear_model import LinearRegression

lr = LinearRegression()  # Initialize the Linear Regression model
lr.fit(x_train, y_train)  # Fit the model to the training data

# Evaluate the model's performance
lr.score(x_test, y_test)  # Check the accuracy of the model on the test data

lr.coef_, lr.intercept_

# Equation will be -> y = -137634.60994912 * x1 + 20502.04918033 * x2^2 + 231288.51045788475
# Calculate the predicted salary for each level in the dataset
prd2 = lr.predict(x)

# Plot the original and predicted salary values
plt.plot(data3["Level"], prd2, color="Red")  # Predicted values
plt.plot(data3["Level"], data3["Salary"])  # Original values
plt.ylabel("Salary")
plt.xlabel("Level")
plt.legend(["Predicted", "Original"])
plt.show()

# Predict the salary for a new level value (e.g., 11)
test = pf.transform([[11]])
predicted_salary = lr.predict(test)
print(predicted_salary)
