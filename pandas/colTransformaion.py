import pandas as pd

data = pd.read_csv("D:\owner(2).csv")
# print(data)
data = pd.read_csv(r"D:\owner(2).csv")  # Ensure the file path is correct

# Add a new column "GetBonus" based on the condition , agar GetBonus nahi bana hoga to ban jayega wrna data updated ho jayega
data.loc[data["bonus"] <= 400, "GetBonus"] = "no bonus"
data.loc[data["bonus"] > 400, "GetBonus"] = "bonus"

# Print the updated DataFrame
# print(data)

#concatenated street and state into one column address
data["address"] = data["o_street"] + ", " + data["o_state"]
# print(data)

data["address"] = data["o_street"].str.capitalize() + ", " + data["o_state"] #first letter must be capital of each street
# print(data)

df = {"Months" : ["January" , "February", "March", "April", "May", "June"]}
a = pd.DataFrame(df)
print(a)