#create model

#import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pickle import dump

#load the data
data = pd.read_csv("heart.csv")
print(data)

#check for null data
print(data.isnull().sum())

#features and target
features = data.drop(["output"],axis="columns")
target = data["output"]
print(features)
print(target)

#train and test
x_train,x_test,y_train,y_test = train_test_split(features.values,target)

#model
model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

#cr
y_pred = model.predict(x_test)
cr = classification_report(y_test,y_pred)
print(cr)

#save the model
with open("heart.pkl","wb") as f:
	dump(model,f)
	print("model saved")








