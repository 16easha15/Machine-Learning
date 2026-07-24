import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("ab.csv")
print(data)

features = data[["A","B"]]

model = KMeans(n_clusters=3,random_state=0)
res = model.fit_predict(features.values)
data["res"]=res
print(data)

a = float(input("enter a "))
b = float(input("enter b "))
d = [[a,b]]
ans=model.predict(d)
print(ans)

