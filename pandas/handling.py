import pandas as pd


data = pd.read_csv("D:\customer(1).csv")
print(data)
print(data.duplicated()) #duplicate data ko de dega
print(data["c_name"].duplicated()) #particular column me agar koi hi duplicate data haii to ussko de dega
print(data["c_state"].duplicated().sum()) #total kitne no. of rows hai jo duplicate values contain krte hai c_state me (kon kon same hai)
print(data.drop_duplicates("c_street")) #sare duplicate values ko drop kr dega bass jo pahla value bachega ussko rakh lega