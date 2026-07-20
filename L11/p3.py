#import lib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor

#load the data
data = pd.read_csv("height_age.csv")

#feature and target
features = data[["HEIGHT","AGE"]]
target = data["WEIGHT"]

#feature scaling
mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)

#find k
k = int(len(data)**0.5)
if k % 2 == 0:
	k = k + 1

#create model
model = KNeighborsRegressor(n_neighbors=k,metric="euclidean")
model.fit(sfeatures,target)

#prediction
he = float(input("enter height "))
ag = float(input("enter age "))
d = [[he,ag]]
sd = mms.transform(d)
ans = model.predict(sd)
print(ans)

#internal
print(model.kneighbors(sd,n_neighbors=k))

#target --> numerical  running  regression
#target --> categorical         classification
	