import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from pickle import dump

#load the data
data = pd.read_csv("used_car_prices.csv")
print(data)

#handle null data
print(data.isnull().sum())
print(data.info())


#features and target
features = data.drop("price",axis="columns")
target = data["price"]

#handle cat data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#MinMaxScaler
mms=MinMaxScaler()
sfeatures= mms.fit_transform(nfeatures.values,target)
print(sfeatures)

#clustering
k=int(len(data)**0.5)
if k % 2 == 0:
	k=k+1

#train and test
x_train,x_test,y_train,y_test=train_test_split(sfeatures,target)


#model creation
model=KNeighborsRegressor(n_neighbors=k,metric ="euclidean")
model.fit(x_train,y_train)

#score
score = model.score(x_test,y_test)
print(score)

#model dump
with open("car.pkl","wb") as f:
	dump(model,f)
	print("model saved")

with open("mms.pkl","wb") as f:
	dump(mms,f)
	print("mms saved")