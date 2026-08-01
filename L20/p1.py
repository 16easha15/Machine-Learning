#import lib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from pickle import dump

#load th data
data = pd.read_csv("diabetes.csv")
print(data)

#check null data
print(data.isnull().sum())
print(data.info())
data.dropna(inplace=True)
print(data.isnull().sum())
print(data.info())
print(data.shape)

#features and target
features = data.drop("Diabetes",axis="columns")
target = data["Diabetes"]
print(features)
print(target)

#handle cat data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#train and test
x_train,x_test,y_train,y_test=train_test_split(nfeatures.values,target)

#model creation
model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

#classification record
y_pred = model.predict(x_test)
cr = classification_report(y_test,y_pred)

#save the model
with open("diabetes.pkl","wb") as f:
	dump(model,f)
	print("model created")









