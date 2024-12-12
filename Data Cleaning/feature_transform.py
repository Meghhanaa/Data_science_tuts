#the main goal of the feature elimination technique is to identify the most important features from the dataset that maximize the model's performance (accuracy).

import pandas as pd
from mlxtend.feature_selection import SequentialFeatureSelector

data = pd.read_csv("D:\data-analytics\diabetes.csv")
print(data.head(5))

# Separate features and target
x = data.iloc[:, :-1]  # Features (all columns except the last one)
y = data["Outcome"]    # Target variable

#no. of feature yaani kitne no. of columns hai ek particular data set me

from sklearn.linear_model import LogisticRegression

# Initialize Logistic Regression
lr = LogisticRegression()  # Ensure convergence with enough iterations

# Apply Sequential Feature Selector

#feature selection -> forward elimination 
fs = SequentialFeatureSelector(estimator=lr, k_features=2, forward=True)
fs = fs.fit(x, y)

# Display selected features and model performance 
#7 feature
print("Selected Feature Indices:", fs.feature_names)
print("Selected Feature Names:", fs.k_feature_names_)
print("Model Accuracy with Selected Features: 2", fs.k_score_)  #0.7591206179441474
#hum jitne no. of k_features lenge usske hisaab se accuracy aayegi 


# Apply Sequential Feature Selector
fs = SequentialFeatureSelector(estimator=lr, k_features=7, forward=True)
fs = fs.fit(x, y)

# Display selected features and model performance
print("Selected Feature Indices:", fs.feature_names)
print("Selected Feature Names:", fs.k_feature_names_)
print("Model Accuracy with Selected Features: 7", fs.k_score_) #0.7734742381801205


# Apply Sequential Feature Selector
# 6 feature
fs = SequentialFeatureSelector(estimator=lr, k_features=6, forward=True)
fs = fs.fit(x, y)

# Display selected features and model performance
print("Selected Feature Indices:", fs.feature_names)
print("Selected Feature Names:", fs.k_feature_names_)
print("Model Accuracy with Selected Features: 6", fs.k_score_) #0.7747899159663865


# Apply Sequential Feature Selector
#5 feature
fs = SequentialFeatureSelector(estimator=lr, k_features=5, forward=True)
fs = fs.fit(x, y)

# Display selected features and model performance
print("Selected Feature Indices:", fs.feature_names)
print("Selected Feature Names:", fs.k_feature_names_)
print("Model Accuracy with Selected Features: 5", fs.k_score_) #0.7708768355827178

# Apply Sequential Feature Selector
# 4 feature
fs = SequentialFeatureSelector(estimator=lr, k_features=4, forward=True)
fs = fs.fit(x, y)

# Display selected features and model performance
print("Selected Feature Indices:", fs.feature_names)
print("Selected Feature Names:", fs.k_feature_names_)
print("Model Accuracy with Selected Features: 4", fs.k_score_) #0.7682964094728801

# Apply Sequential Feature Selector
#3 feature
fs = SequentialFeatureSelector(estimator=lr, k_features=3, forward=True)
fs = fs.fit(x, y)

# Display selected features and model performance
print("Selected Feature Indices:", fs.feature_names)
print("Selected Feature Names:", fs.k_feature_names_)
print("Model Accuracy with Selected Features 3:", fs.k_score_) #0.7683048977166624


#yahan pr hm saare features ko dekh lenge aur jiski accuracy jyda hogi ussko le lenge aur yehi hai forward elemination technique , isssme hum ek ya ek se jyda features ko combine krte hai aur check krte h ki kon sabse jyda accuracy deta hai , jo dega ussko use krenge 