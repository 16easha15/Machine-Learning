import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("age_vehicle.csv")
feature = data[["Age"]]
target = data["Vehicle"]

model = LogisticRegression()
model.fit(feature.values,target)
print(model.classes_)

age = float(input("enter age "))
result = model.predict([[age]])
print(result)

a1 = model.predict_proba([[age]])
a2 = a1.ravel()
bike = round(a2[0]*100,2)
car = round(a2[1]*100,2)
cycle = round(a2[2]*100,2)
print("bike",bike,"car",car,"cycle",cycle)
