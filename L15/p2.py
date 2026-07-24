import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("ab.csv")
print(data)

features = data[["A","B"]]

num,value=[], []
for i in range(1,len(data)+1,1):
	model = KMeans(n_clusters=i)
	model.fit(features.values)
	num.append(i)
	value.append(model.inertia_)

print(num)
print(value)

plt.plot(num,value)
plt.xlabel("Number of clusters ")
plt.ylabel("Inertia ")
plt.show()