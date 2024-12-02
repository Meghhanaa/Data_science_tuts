import numpy as np
import statistics as st

baked_food = [200,300,150,130,200,280,170,188]
a = np.array(baked_food)

print(a)
print(np.mean(a))
print(np.median(a))  #mid values and then average 
print(st.mode(a))
print(np.std(a)) #standard deviation
print(np.var(a)) #variance 

#coefficient of correaltion 
# -1 -> inversely proportional relation & +1 -> strongly correlated
# 0 -> no relation
tobbaco = [30,50,10,30,50,40]
deaths = [100,120,70,100,120,112]

print(np.corrcoef([tobbaco , deaths])) #strongly co related

price = [300,400,500]
sales = [3,2,1]
print(np.corrcoef([price , sales])) #inversly proportional
