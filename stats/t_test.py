import scipy.stats as st
import numpy as np

#q1. a manufacturer claims that the avg weigth of a bag of chips is 150g. a sample of 25 bags is taken and the avg weight is founddd to be 148g , with SD of 5g. Testt the manufacturers claim using a one tailed t-test with a significance level of 5%

# x  = Sample mean = 148
# μ = Population mean (hypothesized mean) = 150
# s = Sample standard deviation = 5
# n = Sample size = 25

# pop_mean = 150 #meu (μ hi population mean haii)
# n = 25
# x = 148  # aur x sample mean hota hai jiske corresponding sd bhi given rhta haii
# sd = 5
# ap = 24 #df = n-1
# # t_tab = 1.1711 #taken from the table on 24 df (df = n-1) where n = 25

# t_tab = st.t.ppf(0.05, ap)
# print(t_tab)

# t_cal = (x - pop_mean)/(sd/np.sqrt(n))
# print("calculated value: ", t_cal)

# if t_cal > t_tab:
#     print("rejected")
# else: 
#     print("accepted")


#Q2. A company wants to test whether there is a difference in productivity between two teams. They randomly select 20 employees from each team and record their productivity scores. The mean productivity score for Team A is 80 with a standard deviation of 5, while the mean productivity score for Team B is 75 with a standard deviation of 6. Test at a 5% level of significance whether there is a difference productivity between the two teams.

# n = 20
# Ax = 80
# As = 5
# Bx = 75
# Bs = 6

# sd = np.sqrt(((np.square(As))+(np.square(Bs)))/n)
# # sd = np.sqrt((As**2+Bs**2/n))
# t_cal = (Ax - Bx) / sd
# print("calculated value:", t_cal)

# t_tab = st.t.ppf(0.975, 2*(n-1)) #In a two-tailed test, you divide this α by 2, yaani 0.05/2 = 0.025 and the value is 1-0.025 = 0.975
# print("tabulated value:", t_tab)

# if t_cal > t_tab:
#     print("rejected")
# else:
#     print("accepted")



#Q3. A company wants to test whether a new training program improves the typing speed of its employees. The typing speed of 20 employees was recorded before and after the training program. The data is given below. Test at a 5% level of significance whether the training program has an effect on the typing speed of the employees.

# Before: 50, 60, 45, 65, 55, 70, 40, 75, 80, 65, 70, 60, 50, 55, 45, 75, 60, 50, 65 
# After: 60, 70, 55, 75, 65, 80, 50, 85, 90, 70, 75, 65, 55, 60, 50, 80, 65, 55,

A = np.array([50, 60, 45, 65, 55, 70, 40, 75, 80, 65, 70, 60, 50, 55, 45, 75, 60, 50, 65, 70])

B = np.array([60, 70, 55, 75, 65, 80, 50, 85, 90, 70, 75, 65, 55, 60, 50, 80, 65, 55, 70, 75])

n = 20
xa = np.mean(A)
xb = np.mean(B)
sda = np.std(A)
sdb = np.std(B)

t_tab = st.t.ppf(1-0.025, n-1)
print("tabulated value:", t_tab)

sd = np.sqrt((np.square(sda) + np.square(sdb)) / n) 
t_cal = (xb - xa)/(sd)
print("calculated value:", t_cal)

if t_cal > t_tab:
    print("rejected")
else:
    print("accepted")