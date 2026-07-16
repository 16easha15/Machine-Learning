#import lib
import pandas as pd
from sklearn.naive_bayes import BernoulliNB

#load the data
data = pd.read_csv("weather_car_result.csv")
print(data)

#features and target
features = data[["Weather","Car"]]
target = data["Result"]

#handle cat data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#model
model = BernoulliNB()
model.fit(nfeatures.values,target)

#prediction
we = int(input("weather: 1 for rainy and 2 for sunny "))
if we == 1:
	d1 = [1,0]
else:
	d1 = [0,1]
car = int(input("car:1 for broken and 2 for working "))
if car == 1:
	d2 =[1,0]
else:
	d2 =[0,1]
d = [d1+d2]
ans = model.predict(d)
print(ans)

print(model.classes_)
print(model.predict_proba(d))