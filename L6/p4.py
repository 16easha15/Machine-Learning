import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("hours_result.csv")
print(data)

feature = data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(feature.values,target)
bO = model.intercept_
b1 = model.coef_[0]
print(model.classes_)

hours = float(input("enter hours "))
result = 1 / (1 + 2.17**(-1*(bO+b1*hours)))
print(result)
if (result>0.5):
	print("pass")
else:
	print("fail")