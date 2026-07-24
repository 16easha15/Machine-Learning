import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("customers.csv")
print(data)

features = data[["Annual_Income","Spending_Score"]]


mms = MinMaxScaler()
sfeatures = mms.fit_transform(features.values)


model =KMeans(n_clusters=5,random_state=0)
res = model.fit_predict(sfeatures)
data["res"]= res
print(data)

c0 = data[data.res==0]	#mi ms
c1 = data[data.res==1]	#hi ls
c2 = data[data.res==2]	#hi hs
c3 = data[data.res==3]	#li ls
c4 = data[data.res==4]	#li hs

income =float(input("enter annual income "))
spending =float(input("enter Spending Score "))
d=[[income,spending]]
sd = mms.transform(d)
ans = model.predict(sd)
match ans:
	case 0 :
		print("mi ms")
	case 1:
		print("hi ls")
	case 2:
		print("hi hs")
	case 3:
		print("li ls")
	case 4:
		print("li hs")