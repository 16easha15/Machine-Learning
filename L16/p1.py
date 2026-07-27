import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = pd.read_csv("cricketers.csv")
print(data)

features = data[["RUNS","WICKETS"]]
mms = MinMaxScaler()
sfeatures = mms.fit_transform(features)
print(sfeatures)

num,val = [],[]
for i in range(1,len(data)+1,1):
	model=KMeans(n_clusters = i)
	model.fit(sfeatures)
	num.append(i)
	val.append(model.inertia_)

print(num)
print(val)
plt.plot(num,val)
plt.show()