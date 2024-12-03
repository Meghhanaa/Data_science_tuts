import matplotlib.pyplot as plt
import numpy as np


# #bar graph

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# #bar() function takes arguments that describes the layout of the bars.
# plt.bar(x,y, width=0.2) #by default verticle graph is drawn, width is defined for verticle graph and height is for horizontal graph
# # plt.barh(x,y, color = 'hotpink') #horizontal graph
# plt.show()

# #histogram

# x = np.random.normal(170, 10, 250) # randomly generate 250 values , where the values will concentrate around 170, and the standard deviation is 10. (170 ke aas paas hi values aayengi randomlyy)

# plt.hist(x)
# plt.show() 

#pie charts

y = np.array([35, 25, 25, 15])
labelsss = ['A','B','C','D']
# plt.pie(y, labels=labelsss)

#explode hum kisi ek ko halka sa bahar dikhane ya hovered dikhane ke liye use krte haii. shadow ussi explode aur pure pie me shadow effect dalta hai

#hum randomly added colors ko apne acc bhii kar skte haii, apna colr array bana ke
plt.pie(y, labels=labelsss, explode=[0.2,0,0,0], shadow=True)
plt.legend(title = "four items") #yeh batane ke liye ki konnsa color kisko show kr rha haii label ke according, title use krte hai legend ko title dene ke liye
plt.show() 