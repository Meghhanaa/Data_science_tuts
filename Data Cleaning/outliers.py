import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"D:\data-analytics\loan.csv")
data

data.describe() #yhan pr mean 1621 hi hai CoapplicantIncome ka aur max value 4667 jo ki mean se bahut jyda hai aur min 0 hai to mean ke paaas hai max ke comparision me, issliye issme bahut saare outier present honge hiii, 

sns.boxplot(x="CoapplicantIncome",data=data) #hum graph me bhi dekh skte haii, kii outliers present haii jo bhi bloack spots hai woh sab hii outliers hai

sns.boxplot(x="ApplicantIncome",data=data) #hum graph me bhi dekh skte haii, kii outliers present haii 

sns.distplot(data["ApplicantIncome"])
#iss wale graph me agar normal distribution hota to nomally start hoke khtm ho jata, lekin issme laast me bahut jyda hi values khich gayi hai jiska mtlb h ki mean value se bahut jyda scatter ho rha haii aurr,  isski tail bahut jyda hai isska mtlb h ki outliers present hai

#outliers ko detect krne ka sabse best tareeka hai boxplot , distplot secondary hai isse bhi kr skte hai

#jab outliers present rhte haii data me toh wrong answers dene lagte hai data jb bhi ML modle train krte hai toh, issliye issko sahi krne ke liye hme outliers remove krna pdta haii,

#OUTLIERS REMOVE KRNE KE LIYE DO METHODS HAI -> Z-SCORE AND IQR METHODS(famous method)

#IQR METHODS ->

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame

# Calculate the first quartile (Q1) - 25th percentile
q1 = data["CoapplicantIncome"].quantile(0.25)

# Calculate the third quartile (Q3) - 75th percentile
q3 = data["CoapplicantIncome"].quantile(0.75)

# Calculate the interquartile range (IQR)
IQR = q3 - q1
print("IQR:", IQR)  # Print the IQR for reference

# Define the lower bound to identify outliers
# 1.5 is a standard multiplier used to determine outliers
minr = q1 - (1.5 * IQR)

# Define the upper bound to identify outliers
maxr = q3 + (1.5 * IQR)
print("Lower Bound:", minr, "Upper Bound:", maxr)  # Print the bounds for reference

# Filter the DataFrame to include only rows where 'CoapplicantIncome' is within the bounds
new_data = data[(data["CoapplicantIncome"] >= minr) & (data["CoapplicantIncome"] <= maxr)]
print("Filtered Data Shape:", new_data.shape)  # Print the shape of the filtered DataFrame

# Plot the boxplot using seaborn to visualize the filtered data
sns.boxplot(x="CoapplicantIncome", data=new_data)

# Show the plot
plt.show()


#removing outliers using z-score or normal distribution, 

minr1 = data["CoapplicantIncome"].mean() - 3*data["CoapplicantIncome"].std()
maxr2 = data["CoapplicantIncome"].mean() + 3*data["CoapplicantIncome"].std()
maxr2 , minr1

new_data2 = data[data["CoapplicantIncome"] <= maxr2] 
sns.boxplot(x="CoapplicantIncome", data=new_data2)
zscore = (data["CoapplicantIncome"] - data["CoapplicantIncome"].mean())/(data["CoapplicantIncome"].std())
zscore
zscore>3
data["zscore"] = zscore
data.head(3)

data[data["zscore"]<3] #yhan pr outlier hat gaye haii, pahle aur baad me data me changes aa gaye hai 