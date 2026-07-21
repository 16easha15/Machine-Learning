#import lib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline

#load data
data = pd.read_csv("loan.csv")
print(data)

#features and target
features = data[["GENDER","OCCUPATION"]]
target = data["DEFAULT"]

#model
model = make_pipeline(
	OneHotEncoder(),
	DecisionTreeClassifier()
	);
model.fit(features.values,target)

#prediction
ge = input("GENDER:FEMALE/MALE ")
oc = input("OCCUPATION:BUSINESS/SALARY ")
d = pd.DataFrame([[ge,oc]])
ans = model.predict(d)
print(ans)