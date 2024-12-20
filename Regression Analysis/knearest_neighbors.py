import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load and preprocess the dataset
data = pd.read_csv("D:\data-analytics\Social_Network_Ads.csv")
data.drop(columns=["User ID", "Gender"], inplace=True)
x = data.iloc[:, :-1]
y = data["Purchased"]

# Initialize and fit the scaler on the entire dataset
sc = StandardScaler()
x_scaled = sc.fit_transform(x)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, random_state=42)

# Initialize and fit the k-NN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

# Function to predict new input data
def predict_new_data(age, estimated_salary):
    new_data = [[age, estimated_salary]]
    new_data_scaled = sc.transform(new_data)  # Scale the new data using the fitted scaler
    prediction = knn.predict(new_data_scaled)
    return prediction[0]

# Example usage with new input data
age = 35
estimated_salary = 35000
prediction = predict_new_data(age, estimated_salary)
print(f"Prediction for Age {age} and Estimated Salary {estimated_salary}: {prediction}")

# Example usage with another new input data
age = int(input("Enter Age: "))
estimated_salary = int(input("Enter Salary: "))
prediction = predict_new_data(age, estimated_salary)
# print(f"Prediction for Age {age} and Estimated Salary {estimated_salary}: {prediction}")

if(prediction):
    print("purchased")
else:
    print("not purchased")

