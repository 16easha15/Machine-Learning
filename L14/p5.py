import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("xy.csv")
print(data)

features = data[["X","Y"]]

model = KMeans(n_clusters=2,random_state=7)
res = model.fit_predict(features.values)
data["res"]=res
print(data)

c0=data[data.res == 0]
c1 = data[data.res == 1]

r1 = model.cluster_centers_
c0x=r1[0][0]
c0y=r1[0][1]
c1x=r1[1][0]
c1y=r1[1][1]

plt.figure(figsize=(12,5))
plt.scatter(c0["X"],c0["Y"],color="red",s=200,label="c0")
plt.scatter(c1["X"],c1["Y"],color="blue",s=200,label="c1")
plt.plot(c0x,c0y,marker="x",markersize=20,label="c0="+str(c0x)+""+str(c0y))
plt.plot(c1x,c1y,marker="x",markersize=20,label="c1="+str(c1x)+""+str(c1y))
plt.grid()
plt.legend(fontsize=20,shadow=True)
plt.show()