import pandas as pd

# data = pd.read_excel("D:\sample_admin.xlsx")
data = pd.read_csv("D:\owner(2).csv")
print(data)

#grouping the particular rows according to the given condition i.e. o_street and o_gender -> batayega kii particulaar street ke andr konse gender ke kitne log hai, count krke bhejegaa, 
#street me gender ke basis me grouping kr diyaa
gp = data.groupby(["o_street","o_gender"]).agg({"o_gender":"count"})
print(gp)

#grouping the particular rows according to the given condition i.e. o_street -> batayega kii particulaar street ke andr kitne log h, count krke bhejegaa, 
gp = data.groupby(["o_street"]).agg({"o_gender":"count"})
print(gp)