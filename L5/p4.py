import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("ps.csv")
feature = data[["Level"]]
target = data["Salary"]

pf = PolynomialFeatures(degree= 4)
pfeature = pf.fit_transform(feature.values)
print(feature)
print(pfeature)

model = LinearRegression()
model.fit(pfeature,target)

level = int(input("enter level "))
plevel = pf.transform([[level]])
salary = model.predict(plevel)
print(salary)
