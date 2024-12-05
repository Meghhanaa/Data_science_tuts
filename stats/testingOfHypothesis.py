import scipy.stats as st
import numpy as np


#Z-TEST = (x_bar - meu)/(sd/sqrt(n))

#a teacher claims that the mean score of the students in his class is greater than 82 with a SD of 20. if a sample of 8 students was selected with a mean score of 90.

x=90 #(sample mean)
u=82 #mean meu
std=20 #standard deviation
n=81 # no. of items(sample size)
ap=0.05 #z ki value jo nikalni pdti h table se (significance level (alpha))

# Calculate the test statistic
z_cal = (x - u) / (std / np.sqrt(n))
print("Calculated Z:", z_cal)

# Find the critical Z value for one-tailed test
z_tab = st.norm.ppf(1 - ap) #jo value given rhti thi table se nikaal ke dete the
print("Tabulated Z:", z_tab)

# Decision
if z_cal > z_tab:
    print("Result: Null hypothesis rejected (teacher's claim is supported).")
else:
    print("Result: Null hypothesis accepted (teacher's claim is not supported).")


#Imagine you work for an e-commerce company, and your team is responsible for analyzing customer purchase data. You want to determine whether a new website design has led to a significant increase in the average purchase amount compared to the old design.

#Data: You have collected data from a random sample of 30 customers who made purchases on the old website design and 30 customers who made purchases on the new website designu have the sample means, sample standard deviations, and sample sizes for both groups.


# Z-TEST = ({[(x_bar(new website) - x_bar(old website))] - [(u(new website) - u(old website))]})/(sd/sqrt(n))


old_data = np.array([45.2, 42.8, 38.9, 43.5, 41.0, 44.6, 40.5, 42.7, 39.8, 41.4, 44.3, 39.7, 42.1, 40.6, 43.0, 42.2, 41.5, 39.6, 44.0, 43.1, 38.7, 43.9, 42.0, 41.9, 42.8, 43.7, 41.3, 40.9, 42.5, 41.6])

new_data = np.array([48.5, 49.1, 50.2, 47.8, 48.7, 49.9, 48.0, 5015, 49.8, 49.6, 48.2, 48.9, 49.7, 50.3, 49.4, 50.1, 48.6, 48.3, 49.0, 50.0, 48.4, 49.3, 49.5, 48.8, 50.6, 50.4, 48.1, 49.2, 50.7, 50.8])

pop_std = 2.5
n_sp = len(new_data)
alpha = 0.05

mean_new = np.mean(new_data)
mean_old = np.mean(old_data)

z_cal = (mean_new - mean_old)/(pop_std/np.sqrt(n_sp))
print("calculated z_cal:",z_cal)

z_tab = st.norm.ppf(1-alpha)
print("tabulated value: ",z_tab)

if z_cal > z_tab:
    print("rejected")
else:
    print("accpeted")