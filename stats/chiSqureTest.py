import scipy.stats as st
import numpy as np

#chi sqr test = χ = ∑ (fo - fe)^2/fe

#Q1. A fair die is rolled 120 times and the following results are obtained:
# Face 1: 22 times
# Face 2: 17 times
# Face 3: 20 times
# Face 4: 26 times
# Face 5: 22 times
# Face 6: 13 times
# Test at a 5% level of significance whether the die is fair.

# n = 120
# fo = np.array([22,17,20,26,22,13])
# fe = np.array([20,20,20,20,20,20]) 

# fre = fo - fe
# ans= (fre**2) / fe 
# chi_cal = np.sum(ans)

# print("chi sqr calculated value: ", chi_cal)

# chi_tab = 11.07
# print("chi sqr calculated value: ", chi_tab)

# if chi_cal > chi_tab:
#     print("Rejected")
# else:
#     print("Accepted")

#Q2. A study was conducted to investigate whether there is a relationship between gender and the preferred genere of the music. a sample of 235 people was selected, and the data collected is shown below. Test at a 5% level of the significance whether there is a significant association between gender and music preference.

# male = 40,45,25,10
# female = 35,30,20,30

male = np.array([40,45,25,10])
female = np.array([35,30,20,30])

fo = np.array([40,45,25,10,35,30,20,30])

sum_male =  np.sum(male)
sum_female =  np.sum(female)
sum_row = np.array([sum_male , sum_female])
sum_col = male + female

print(sum_row)
print(sum_col)
fe = []

for i in sum_row:
    for j in sum_col:
        val = (i*j)/235
        fe.append(val)

print("Expected freq: ")
print(fe)

chi_cal = np.sum(np.array((fo - fe)**2 / fe))

print("chi sqr calculated value: ", chi_cal)

chi_tab = 13.78
print("chi sqr tabulated value: ", chi_tab)

if chi_cal > chi_tab:
    print("Rejected")
else:
    print("Accepted")
