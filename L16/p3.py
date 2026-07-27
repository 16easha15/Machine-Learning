import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

data=pd.read_csv("cricketers.csv")
print(data)

features=data[["RUNS","WICKETS"]]
mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)
print(sfeatures)

model=KMeans(n_clusters=2,random_state=0)
res = model.fit_predict(sfeatures)
data["res"]=res
print(data)

runs = int(input("Enter runs: "))
wickets = int(input("Enter Wickets: "))
d = [[runs,wickets]]
sd = mms.transform(d)
ans=model.predict(d)
if ans == 1:
	print("Batsman")
else:
	print("Bowler")