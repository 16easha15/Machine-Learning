#internal working using sigmoid

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("age_sub.csv")
feature = data[["age"]]
target = data["sub"]

model = LogisticRegression()
model.fit(feature.values,target)
print(model.classes_)

b0=model.intercept_
b1=model.coef_[0]

age = float(input("enter age "))
result = 1/(1+2.71**(-1*(b0+b1*age)))
print(result)

if result>=0.5:
	print("Yes")
else:
	print("No")
