import pandas as pd

dict = {"fruits": ["mango","banana","apples","kiwi"],
        "price":[100,50,90,75],
        "quan": [15,10,15,20]}

df = pd.DataFrame(dict)
# print(df)

df2 = df.copy()
# print(df2)

df2.loc[0, "price"] = 120
df2.loc[1, "price"] = 70
df2.loc[2, "price"] = 100
df2.loc[0, "quan"] = 20
df2.loc[1, "quan"] = 15
df2.loc[2, "quan"] = 25
df2.loc[3, "quan"] = 40
# print(df2)

# print(df.compare(df2)) 
# #dono jagh compare krke bata dega ki pahle price me kya the self me aur ab kya hai other me, similarly quan me, kyuki ab quan me saare hi rows me changes ho rahe hai issliye , price wale me jaha pr koi chnges nahi hai waha pr Nan aa gaya haii

# print(df.compare(df2, align_axis=0))
# print(df.compare(df2, keep_shape=True))


#pivoting and melting


# Original dictionary
d = {
    "keys": ["k1", "k2", "k1", "k3"],
    "names": ["john", "ben", "david", "peter"],
    "house": ["red", "blue", "blue", "yellow"],
    "grades": [3 , 4 , 4 , 9]
}

# Create DataFrame
pd3 = pd.DataFrame(d)
print("Original DataFrame:")
print(pd3)

# Using pivot with aggregation to handle duplicates

piv = pd3.pivot(index="keys", columns="names", values=["house","grades"])
print("\nPivoted DataFrame:")
print(piv)

# Alternative solution: Using pivot_table with aggregation
pivot_table_df = pd3.pivot_table(
    index="keys", columns="names", values="house", aggfunc=lambda x: ", ".join(x)
)
print("\nPivot Table (handles duplicates with aggregation):")
print(pivot_table_df)


#Melting

melted_df = pd.melt(pd3, id_vars=["names"], value_vars=["house","grades"], var_name="houses&grades")
print("\nMelted DataFrame:")
print(melted_df)

