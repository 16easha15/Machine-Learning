#import lib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

#load the data
data = pd.read_csv("health.csv")
print(data)

#features and target
features = data[["Weight","Height"]]
target = data["Class"]

#feature scaling
mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)
print(features)
print(sfeatures)

#find k
k = int(len(data)**0.5)
if k % 2==0:
	k=k + 1
#model
model = KNeighborsClassifier(n_neighbors=k,metric="euclidean")
model.fit(sfeatures,target)

#predict 
we = float(input("Enter weight(kg) "))
he = float(input("Enter Height(cm) "))
d = [[we,he]]
sd = mms.transform(d)
ans = model.predict(sd)
print(ans)

#internal
print(model.kneighbors(sd,n_neighbors = k))
