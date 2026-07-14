import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("hours_result.csv")
print(data)

feature =data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(feature.values,target)

hours = float(input("enter hours "))
result = model.predict([[hours]])
print(result)