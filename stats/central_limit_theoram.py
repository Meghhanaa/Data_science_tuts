import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [np.random.randint(0,100) for i in range(10000)]
# print(data)
print("mean of the data:" , np.mean(data))

pop_table = pd.DataFrame({"data":data})
# sns.kdeplot(x="data", data=pop_table) #yeh thoda faila faila sa tha

# plt.show()

#jo bhi hmare paas sample data the usse hmne chhote chhote sample data nikaal liye aur un chote chote sample data ka hmne mean nikaal ke sample_mean me store kr liye hai, aur uss sample_mean ka dataframe bana ke ussme analysis krenge
sample_mean = []
for i in range(70):
    sample_data = []
    for j in range(500):
        sample_data.append(np.random.choice(data))
    sample_mean.append(np.mean(sample_data))

print("sample mean of the sample data: ")
print(sample_mean)
print("mean of sample mean:", np.mean(sample_mean)) #pahle kisi data ka sample mean aur abhi ka mean dono same hai

sample_M = pd.DataFrame({"sample_mean": sample_mean})
sns.kdeplot(x="sample_mean", data=sample_M) #yahan pr data normally distributed hogya haiii
plt.show()
