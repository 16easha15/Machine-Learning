#drop missing/null data
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("aqp_july26.csv")
print(data)

print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())
print(data)

feature = data[["qty"]]
target = data["price"]

model = LinearRegression()
model.fit(feature.values,target)

qty = float(input("enter qty "))
price = model.predict([[qty]])
print(price)