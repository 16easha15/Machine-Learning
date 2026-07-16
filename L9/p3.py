import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv("student_exam.csv")
features = data.drop(["pass_exam"],axis="columns")
target = data["pass_exam"]

model = GaussianNB()
model.fit(features.values,target)

study = float(input("enter number of hours studied "))
sleep = float(input("enter number of hours slept "))
stress = float(input("enter stress level "))
d = [[study]+[sleep]+[stress]]
print(model.predict(d))
print(model.classes_)
print(model.predict_proba(d))