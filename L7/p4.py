#internal working->using predict_proba

import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("age_sub.csv")
feature = data[["age"]]
target = data["sub"]

model = LogisticRegression()
model.fit(feature.values,target)

age=float(input("enter age "))
result = model.predict([[age]])
print(result)

a1 = model.predict_proba([[age]]) #2D List
a2 = a1.ravel()			  #1D List
print(a2)

pno=round(a2[0]*100,2)		#no probability
pyes=round(a2[1]*100,2)		#yes probability

print("pno = ",pno , "%","pyes = ",pyes, "%")
