import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data=pd.read_csv("customers.csv")
print(data)

features = data[["Annual_Income","Spending_Score"]]
print(features)

mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)
print(sfeatures)

num,values = [],[]
for i in range(1,10,1):
	model=KMeans(n_clusters=i)
	model.fit(sfeatures)
	num.append(i)
	values.append(model.inertia_)

plt.plot(num,values)
plt.show()