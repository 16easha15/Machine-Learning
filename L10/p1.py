#import lib 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

#load the data
data = pd.read_csv("tshirt.csv")
print(data)

#features and target
features  = data[["Height(cm)", "Weight(kg)"]]
target = data["T-Shirt Size"]

#feature scaling
mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)
print(features)
print(sfeatures)

#find k
k = int(len(data)**0.5)
if k % 2 == 0:
	k = k + 1

#model
model = KNeighborsClassifier(n_neighbors = k,metric ="euclidean")
model.fit(sfeatures,target)

#predict
he = float(input("enter height in cm "))
we = float(input("enter weight in kg "))
d = [[he,we]]
sd = mms.transform(d)
ans = model.predict(sd)
print(ans)

#internal
print(model.kneighbors(sd,n_neighbors = k))