import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("xy.csv")
print(data)

features = data[["X","Y"]]
model = KMeans(n_clusters=2,random_state=7)
res = model.fit_predict(features.values)
data["res"] = res
print(data)

x = float(input("enter x "))
y = float(input("enter y "))
ans = model.predict([[x,y]])
if ans == 0:
	print("c0")
else:
	print("c1")