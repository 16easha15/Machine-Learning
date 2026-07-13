import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("pap.csv")

features = data[["place","area"]]
target = data["price"]
nfeatures = pd.get_dummies(features)
print(features)

model = LinearRegression()
model.fit(nfeatures.values,target)

area = float(input("enter area "))
place = int(input("1.karjat , 2.Khandala ,3.Lonavla "))
if place == 1:
	d = [[area,1,0,0]]
elif place == 2:
	d = [[area,0,1,0]]
else:
	d = [[area,0,0,1]]
price = model.predict(d)
print(price)