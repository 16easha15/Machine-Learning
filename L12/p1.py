#import lib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#load the data
data = pd.read_csv("loan.csv")
print(data)

#features and target
features = data[["GENDER","OCCUPATION"]]
target = data["DEFAULT"]

#handle categorical data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#model
model = DecisionTreeClassifier()
model.fit(nfeatures.values,target)

#prediction
ge = int(input("GENDER: 1 for FEMALE and 2 for MALE "))
if ge == 1:
	d1 = [1,0]
else:
	d1 = [0,1]
oc = int(input("OCCUPATION: 1 for BUSINESS and 2 for SALARY "))
if oc == 1:
	d2 = [1,0]
else:
	d2 = [0,1]
d = [d1+d2]
ans = model.predict(d)
print(ans)