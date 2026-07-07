import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("emp_salary.csv")
feature = data[["exp"]]
target = data["sal"]

model = LinearRegression()
model.fit(feature.values,target)

exp = float(input("enter exp "))
sal = model.predict([[exp]])
print(sal)