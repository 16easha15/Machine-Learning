import pandas as pd

data = pd.read_csv("student.csv")
print(data.isnull().sum())
data.fillna({"Gender":"unknown"},inplace=True)
print(data.isnull().sum())

print(data["Math_Marks"].skew())
data.fillna({"Math_Marks":data["Math_Marks"].median()},inplace=True)
print(data.isnull().sum())

print(data["English_Marks"].skew())
data.fillna({"English_Marks":data["English_Marks"].median()},inplace=True)
print(data.isnull().sum())

print(data["Attendance"].skew())
data.fillna({"Attendance":data["Attendance"].mean()},inplace=True)
print(data.isnull().sum())