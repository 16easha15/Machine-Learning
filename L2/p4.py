import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("emp_salary.csv")
feature = data[["exp"]]
target = data["sal"]

model = LinearRegression()
model.fit(feature.values,target)

b0 = model.intercept_
b1 = model.coef_[0]
print("b0 = ",b0)
print("b1 =",b1)