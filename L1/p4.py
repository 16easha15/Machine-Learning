#predict ka internal formula

import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("housingdata.csv")

feature = data[["area"]]
target = data["price"]

model = LinearRegression()
model.fit(feature.values,target)

area = float(input("Enter Area "))
bO = model.intercept_
b1 = model.coef_[0]
price = bO+b1*area
print("price = ",price)