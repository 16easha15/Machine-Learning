import pandas as pd 
from sklearn.linear_model import LinearRegression

data = pd.read_csv("emp_salary.csv")
feature = data[["exp"]]
target = data["sal"]

model = LinearRegression()
model.fit(feature.values,target)

exp = float(input("enter exp "))
b0 = model.intercept_
b1 = model.coef_[0]
sal = b0+b1*exp
print(sal)