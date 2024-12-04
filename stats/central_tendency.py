# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the dataset
# Make sure to replace the file path with the correct one
data = pd.read_csv("/data-analytics/titanic.csv")

# Calculate the mean of the 'Age' column
# NaN values are automatically ignored in numpy's mean function
mean_age = np.mean(data["Age"])

# Calculate the median of the 'Age' column
# Use np.median and drop NaN values to ensure accurate calculation
median_age = np.median(data["Age"].dropna())

# Calculate the mode of the 'Age' column
# Use pandas' mode() function which returns the most frequent value
mode_age = data["Age"].mode()[0]  # Taking the first mode in case of multiple modes

# Print calculated values
print(f"Mean of the age: {mean_age}")
print(f"Median of the age: {median_age}")
print(f"Mode of the age: {mode_age}")

# Create a histogram to visualize the age distribution
# The 'edgecolor' parameter adds a border to each bar for better visual clarity
sns.histplot(
    x="Age",                # Data column to plot
    data=data,              # Dataset
    bins=[i for i in range(0, 81, 10)],  # Specify bin intervals (0 to 80, step 10)
    edgecolor="black"       # Add black borders to the histogram bars
)

# Add vertical lines for mean, median, and mode
# These lines help identify the central tendency measures on the histogram
plt.axvline(mean_age, color="red", linestyle="--", label=f"Mean: {mean_age:.2f}")
plt.axvline(median_age, color="blue", linestyle="-.", label=f"Median: {median_age:.2f}")
plt.axvline(mode_age, color="green", linestyle=":", label=f"Mode: {mode_age:.2f}")

# Add labels, title, and legend for better understanding
plt.title("Distribution of Age")  # Set the title of the histogram
plt.xlabel("Age")                 # Label the x-axis
plt.ylabel("Frequency")           # Label the y-axis
plt.legend()                      # Add a legend to explain the lines

# Display the plot
plt.show()


# sns.histplot(x="fare", data=data, bins=[i for i in range(0,81,10)])
# plt.pl
