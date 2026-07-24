import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = pd.read_csv("customers.csv")
print(data)

features = data[["Annual_Income","Spending_Score"]]
print(features)

mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)
print(sfeatures)

model =KMeans(n_clusters=5,random_state=0)
res = model.fit_predict(sfeatures)
data["res"]= res

c0 = data[data.res==0]	#mi ms
c1 = data[data.res==1]	#hi ls
c2 = data[data.res==2]	#hi hs
c3 = data[data.res==3]	#li ls
c4 = data[data.res==4]	#li hs
cc0=model.cluster_centers_[0]
cc1=model.cluster_centers_[1]
cc2=model.cluster_centers_[2]
cc3=model.cluster_centers_[3]
cc4=model.cluster_centers_[4]


plt.figure(figsize=(12,5))
plt.scatter(c0["Annual_Income"],c0["Spending_Score"],s=200,label="c0")
plt.scatter(c1["Annual_Income"],c1["Spending_Score"],s=200,label="c1")
plt.scatter(c2["Annual_Income"],c2["Spending_Score"],s=200,label="c2")
plt.scatter(c3["Annual_Income"],c3["Spending_Score"],s=200,label="c3")
plt.scatter(c4["Annual_Income"],c4["Spending_Score"],s=200,label="c4")

plt.xlabel("Income")
plt.ylabel("Score")
plt.grid()
plt.legend(fontsize=20,shadow=True)
plt.show()