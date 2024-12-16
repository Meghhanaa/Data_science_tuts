import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load the dataset
data = pd.read_csv(r"D:\data-analytics\Housing.csv")
data.head(5)

# Visualize correlations in the dataset
sns.heatmap(data=data.corr(), annot=True)
plt.show()

# Select categorical columns to be one-hot encoded
en_data = data[["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]]

# Perform one-hot encoding for non-numeric columns
ohe2 = OneHotEncoder(drop="first")  
ar2 = ohe2.fit_transform(en_data).toarray()

# Convert the encoded array back to a DataFrame
reduced_df = pd.DataFrame(ar2, columns=ohe2.get_feature_names_out(en_data.columns))
print(reduced_df)

# Drop the original non-numeric columns from the original dataset
data = data.drop(columns=en_data.columns)

# Concatenate the original dataset (without the non-numeric columns) with the new encoded DataFrame
data = pd.concat([data, reduced_df], axis=1)

# Encode 'furnishingstatus' using LabelEncoder
le = LabelEncoder()
data["furnishingstatus"] = le.fit_transform(data["furnishingstatus"])

# Separate the features (independent variables) and target (dependent variable)
x = data.iloc[:, 1:]
y = data["price"]

# Initialize the StandardScaler
sc = StandardScaler()

# Fit the scaler to the features
sc.fit(x)

# Transform the features and convert them back to a DataFrame
x = pd.DataFrame(sc.transform(x), columns=x.columns)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(x_train, y_train)
linear_accuracy = lr.score(x_test, y_test) * 100  # Calculate accuracy
print(f"Linear Regression Accuracy: {linear_accuracy:.2f}%")

# Plotting the coefficients of Linear Regression
plt.figure(figsize=(20, 7))
plt.bar(x.columns, lr.coef_)
plt.title("Linear Regression Coefficients")
plt.xlabel("Columns")
plt.ylabel("Coefficients")
plt.show()

# Lasso Regression
la = Lasso(alpha=0.05)
la.fit(x_train, y_train)
lasso_accuracy = la.score(x_test, y_test) * 100  # Calculate accuracy
print(f"Lasso Regression Accuracy: {lasso_accuracy:.2f}%")

# Plotting the coefficients of Lasso Regression
plt.figure(figsize=(20, 7))
plt.bar(x.columns, la.coef_)
plt.title("Lasso Regression Coefficients")
plt.xlabel("Columns")
plt.ylabel("Coefficients")
plt.show()

# Ridge Regression
ri = Ridge(alpha=10)
ri.fit(x_train, y_train)
ridge_accuracy = ri.score(x_test, y_test) * 100  # Calculate accuracy
print(f"Ridge Regression Accuracy: {ridge_accuracy:.2f}%")

# Plotting the coefficients of Ridge Regression
plt.figure(figsize=(20, 7))
plt.bar(x.columns, ri.coef_)
plt.title("Ridge Regression Coefficients")
plt.xlabel("Columns")
plt.ylabel("Coefficients")
plt.show()

# Calculate and display errors for each case
lr_mae = mean_absolute_error(y_test, lr.predict(x_test))
lr_mse = mean_squared_error(y_test, lr.predict(x_test))
lr_rmse = np.sqrt(lr_mse)
print(f"Linear Regression MAE: {lr_mae:.2f}, MSE: {lr_mse:.2f}, RMSE: {lr_rmse:.2f}")

la_mae = mean_absolute_error(y_test, la.predict(x_test))
la_mse = mean_squared_error(y_test, la.predict(x_test))
la_rmse = np.sqrt(la_mse)
print(f"Lasso Regression MAE: {la_mae:.2f}, MSE: {la_mse:.2f}, RMSE: {la_rmse:.2f}")

ri_mae = mean_absolute_error(y_test, ri.predict(x_test))
ri_mse = mean_squared_error(y_test, ri.predict(x_test))
ri_rmse = np.sqrt(ri_mse)
print(f"Ridge Regression MAE: {ri_mae:.2f}, MSE: {ri_mse:.2f}, RMSE: {ri_rmse:.2f}")


df = pd.DataFrame({ "col_name": x.columns, "LinearRegression": lr.coef_, "Lasso": la.coef_, "Ridge": ri.coef_ })
print(df) #to check the relationship between all the coefficient of all regularization