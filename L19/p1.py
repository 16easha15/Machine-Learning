#import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pickle import dump

#load data
data=pd.read_csv("house_rent.csv")
print(data)

#handle null data
print(data.isnull().sum())
print(data.info())

#features and target
features = data.drop("rent",axis="columns")
target = data["rent"]
print(features)
print(target)

#handle cat data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#train and test
x_train,x_test,y_train,y_test = train_test_split(nfeatures.values,target)

#model creation
model = LinearRegression()
model.fit(x_train,y_train)

#score
score = model.score(x_test,y_test)
print(score)

#save the model
with open("rent.pkl","wb") as f:
	dump(model,f)
	print("model saved")

