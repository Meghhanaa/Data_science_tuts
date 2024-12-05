n = 20
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