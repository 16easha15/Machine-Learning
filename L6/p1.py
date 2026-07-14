#import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#load the data
data = pd.read_csv("rent.csv")
print(data.shape)
print(data.head())
print(data.tail())

#check for null data
print(data.isnull().sum())

#handle null data
print(data["area"].skew())
print(data["bedrooms"].skew())
data.fillna({
		"area":data["area"].mean(),
		"bedrooms":data["bedrooms"].mean()	
	},
	inplace=True)
print(data.isnull().sum())

#features and target
features=data[["location","area","bedrooms"]]
target=data["price"]

#handle categorical data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

#train and test
x_train,x_test,y_train,y_test = train_test_split(nfeatures.values,target)

#model
model = LinearRegression()
model.fit(x_train,y_train)

#score
score = model.score(x_test,y_test)
print(score)

#predict
area = float(input("enter area : "))
bedrooms = float(input("enter number of  bedrooms: "))
location = int(input(" 1.bandra ,2.borivali,3. dadar,4. thane "))
if location == 1:
	d = [[area,bedrooms,1,0,0,0]]
elif location == 2:
	d = [[area,bedrooms,0,1,0,0]]
elif location == 3:
	d = [[area,bedrooms,0,0,1,0]]
else:
	d = [[area,bedrooms,0,0,0,1]]
price = model.predict(d)
print(price)
