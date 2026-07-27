import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

data = pd.read_csv("cricketers.csv")
print(data)

features = data[["RUNS","WICKETS"]]
print(features)

model = make_pipeline(
	MinMaxScaler(),
	KMeans(n_clusters=2,random_state=0)
	)
res=model.fit_predict(features.values)
data["res"]=res

runs=float(input("Enter runs: "))
wickets=float(input("enter wickets: "))
d=[[runs,wickets]]
ans=model.predict(d)
if ans == 1:
	print("Batsman")
else:
	print("Bowler")