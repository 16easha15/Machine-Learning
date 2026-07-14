#soln using LR
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("age_sub.csv")
feature = data[["age"]]
target = data["sub"]

model = LogisticRegression()
model.fit(feature.values,target)

age = float(input("enter age "))
result = model.predict([[age]])
print(result)