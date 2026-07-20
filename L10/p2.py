#import lib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline

#load the data
data = pd.read_csv("tshirt.csv")
print(data)

#features and target
features  = data[["Height(cm)", "Weight(kg)"]]
target = data["T-Shirt Size"]

#find k
k = int(len(data)**0.5)
if k % 2 == 0:
	k = k+1

#model
model = make_pipeline(MinMaxScaler(),KNeighborsClassifier(n_neighbors = k,metric="euclidean"))
model.fit(features.values,target)

#predict
he = float(input("enter height in cm "))
we = float(input("enter weight in kg "))
d = [[he,we]]
ans = model.predict(d)
print(ans)
