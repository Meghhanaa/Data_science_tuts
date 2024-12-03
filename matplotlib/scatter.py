import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#we can color each dot as required

# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75]) #we can add sizes to each of the point
# plt.scatter(x,y, color = colors, s = sizes)
# plt.colorbar() #used to add the colorbar vertically in the graph



# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'hotpink')

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = 'cyan')


#alpha is used to adjust the transparency of the dots with the alpha argument.
#alpha ranges between the 0 to 1, 0 means very transparent(invisible) and 1 means near to solid

# plt.scatter(x,y,alpha=0)

# plt.show()

#Create random arrays with 100 values for x-points, y-points, colors and sizes:
m = np.random.randint(100, size=(100))
n = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(m, n, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()