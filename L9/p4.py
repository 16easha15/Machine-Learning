#import lib
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

#load the data
data = pd.read_csv("sna.csv")
print(data)

#check and handle null data
print(data.isnull().sum())

#features and target
features = data.drop(["Purchased","User ID"],axis="columns")
target = data["Purchased"]

#handle categorical data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#train and test
x_train,x_test,y_train,y_test = train_test_split(nfeatures.values,target)

#model creation
model = GaussianNB()
model.fit(x_train,y_train)

#classification report
y_pred = model.predict(x_test)
print(data["Purchased"].value_counts())
cr = classification_report(y_test,y_pred)
print(cr)

#prediction
age = float(input("enter age "))
salary = float(input("enter salary "))
Gender = float(input("Gender--> 1 female and 2 male "))
if Gender == 1:
	d = [[age,salary,1,0]]
else:
	d = [[age,salary,0,1]]
ans = model.predict(d)
print(ans)
print(model.predict_proba(d))




