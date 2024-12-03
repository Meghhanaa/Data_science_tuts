import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints) #ek straight line ban jayegiii
# plt.show()

# pt = np.array([30, 8, 15, 10])

# plt.plot(pt, marker = 'o') #filled circle will be used as a markers in the points of the marksz
# plt.show()

# #to make the lined with the particular line style
# plt.plot(pt, linestyle = 'dotted', linewidth = '5.5', c = 'red')
# plt.show()

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# #ek hi graph me do lines ko plot krna
# plt.plot(y1) 
# plt.plot(y2)

# plt.show()

# x1 = np.array([10,30,15,5])
# x2 = np.array([3,8,2,5])
# y1 = np.array([9,30,10,25])
# y2 = np.array([11,35,25,15])
# plt.plot(x1,y1,x2,y2)
# plt.show()


#labels and titles

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([220, 290, 200, 170, 180, 298, 200, 310, 320, 330])


# plt.plot(x,y)
# plt.title("learning matplotlib", loc='right')
# plt.xlabel("X-LABEL", fontdict={'color':'red', 'size':15})
# plt.ylabel("Y-LABEL", fontdict={'color':'purple', 'size':25})
# # plt.grid(axis='y') #maths jaisa dabba dabba laane ke ;iye grid use krte hai, ussme agar bas horizontal line chahiye to axis = 'y' and verticle line chahiye to axis = 'x' karna hai

# plt.grid(color = 'green', linestyle = 'dotted', linewidth = 1) #grid lines ko style dene ke liyee

# plt.show()



#displaying multiple plots

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.title("BOSS")
# plt.subplot(1,2,1) #the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(2,2,1) # the figure has 2 rows, 2 cols, and this is the 1st plot
plt.plot(x,y)



#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.title("EMPLOYEES")
# plt.subplot(1,2,2) #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(2,2,2) # the figure has 2 rows, 2 cols, and this is the 2nd plot
plt.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.title("SALES")
# plt.subplot(1,2,2) #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(2,2,3) # the figure has 2 rows, 2 cols, and this is the 2nd plot
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.title("INCOME")
# plt.subplot(1,2,2) #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(2,2,4) # the figure has 2 rows, 2 cols, and this is the 2nd plot
plt.plot(x,y)

plt.suptitle("my super title")
plt.show()

#we can draw many plots and graphs requiredd we just need to add as many rows as cols required