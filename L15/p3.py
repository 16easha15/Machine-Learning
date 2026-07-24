import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("ab.csv")
print(data)

features = data[["A","B"]]

model = KMeans(n_clusters=3,random_state=0)
res =model.fit_predict(features.values)
data["res"]=res
print(data)

c0 = data[data.res == 0]
c1 = data[data.res == 1]
c2 = data[data.res == 2]
cc0=model.cluster_centers_[0]
cc1=model.cluster_centers_[1]
cc2=model.cluster_centers_[2]
print(cc0)
print(cc1)
print(cc2)

plt.figure(figsize=(12,5))
plt.scatter(c0["A"],c0["B"],color="red",s=200,label="Cluster 0")
plt.scatter(c1["A"],c1["B"],color="green",s=200,label="Cluster 1")
plt.scatter(c2["A"],c2["B"],color="blue",s=200,label="Cluster 2")

plt.plot(cc0[0],cc0[1],marker="x",markersize=20,label="cc0"+str(cc0[0])+""+str(cc0[1]))
plt.plot(cc1[0],cc1[1],marker="x",markersize=20,label="cc1"+str(cc1[0])+""+str(cc1[1]))
plt.plot(cc2[0],cc2[1],marker="x",markersize=20,label="cc2"+str(cc2[0])+""+str(cc2[1]))

plt.grid()
plt.legend(fontsize=20,shadow=True)
plt.show()