import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Load the dataset
data = pd.read_csv(r"D:\data-analytics\Social_Network_Ads.csv")

# Display the first 5 rows of the dataset
print(data.head(5))

# Drop unnecessary columns
data.drop(columns=["User ID", "Gender"], inplace=True)

# Separate the features and the target variable
x = data.iloc[:, :-1]  # Features
y = data["Purchased"]  # Target

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(y_train)

# Initialize and fit the Logistic Regression model
lr = LogisticRegression()
lr.fit(x_train, y_train)

# Generate predictions and evaluate the model
y_pred = lr.predict(x_test)

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualize the confusion matrix
sns.heatmap(cm, annot=True, fmt='d')  # 'fmt' ensures integer formatting for the annotations
plt.title("Confusion Matrix")
plt.show()

# Calculate and display the recall score
rec = recall_score(y_test, y_pred)
print(f"Recall Score: {rec:.2f}")

# Calculate and display the precision score
precision = precision_score(y_test, y_pred)
print(f"Precision Score: {precision:.2f}")

# Calculate and display the F1 score
f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1:.2f}")
