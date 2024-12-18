import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv(r"D:\data-analytics\placement-dataset.csv")
dataset.drop(columns=["Unnamed: 0"], inplace=True)  # Drop the unnecessary column
dataset.head(10)  # Display the first 10 rows of the dataset

# Visualize the relationship between CGPA and IQ, colored by placement status
sns.scatterplot(x="cgpa", y="iq", hue="placement", data=dataset)

# KDE plot to check if CGPA follows a normal distribution
sns.kdeplot(data=dataset["cgpa"])  # check krna hai ki cgpa normml distribution me hai ya nahi
plt.title("KDE Plot of CGPA")
plt.show()

# KDE plot to check if IQ follows a normal distribution
sns.kdeplot(data=dataset["iq"])  # check krna hai ki iq normml distribution me hai ya nahi
plt.title("KDE Plot of IQ")
plt.show()

# Separate the features and target variable
x = dataset.iloc[:, :-1]  # Features (all columns except the last one)
y = dataset["placement"]  # Target (the last column)
y

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train

# ab jaise ki dono lagbhag lagbhag normally distributed hai, toh wha pr hum gaussian naive bayes theoram use krenge
# Since both CGPA and IQ are approximately normally distributed, we'll use Gaussian Naive Bayes

# GAUSSIAN NB
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
gau = GaussianNB()
gau.fit(x_train, y_train)
gau.score(x_test, y_test)  # 85% of the accuracy in the testing data, using the gaussian theorem
gau.predict([[4.8, 141.0]])
gau.score(x_train, y_train)  # 91% accuracy in the training data, using the gaussian theorem

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.to_numpy(), y.to_numpy(), clf=gau)

# MULTINOMIAL NB
mul = MultinomialNB()
mul.fit(x_train, y_train)
mul.score(x_test, y_test), mul.score(x_train, y_train)

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.to_numpy(), y.to_numpy(), clf=mul)

# BERNOULLI NB
ber = BernoulliNB()
ber.fit(x_train, y_train)  # bernoulii me sabse bekaar accuracy aayi hai as compared to all other, issliye jab bhiii data 0 1 ke form me ho tbhi bernouli use krna chahiye

ber.score(x_test, y_test), ber.score(x_train, y_train)

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.to_numpy(), y.to_numpy(), clf=ber)
