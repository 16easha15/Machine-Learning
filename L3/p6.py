#import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pickle import dump

#load the data
data = pd.read_csv("cdj_july26.csv")
print(data)
print(data.head())
print(data.tail())

#check for null data
print(data.isnull().sum())

#features and target
features = data[["R&D Spend","Administration","Marketing Spend"]]
target=data["Profit"]

#train and test
x_train,x_test,y_train,y_test = train_test_split(features.values,target)

#model
model = LinearRegression()
model.fit(x_train,y_train)

#performance
score = model.score(x_test,y_test)
print(score*100)

#save the model
with open("bpe.pkl","wb") as f:
	dump(model,f)
	print("model saved")
