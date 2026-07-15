import pandas as pd
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("weather_play.csv")
print(data)

feature = data[["Weather"]]
target = data["Play"]
nfeature = pd.get_dummies(feature)
print(nfeature)

model = BernoulliNB()
model.fit(nfeature.values,target)

weather = int(input("1. Overcast,2. Rainny and 3. Sunny "))
if weather == 1:
	d = [[1,0,0]]
elif weather == 2:
	d = [[0,1,0]]
else:
	d = [[0,0,1]]

ans = model.predict(d)
print(ans)
print(model.classes_)

a1 = model.predict_proba(d)
a2 = a1.ravel()
pno = round(a2[0]*100,2)
pyes = round(a2[1]*100,2)
print("pno = ",pno,"%","pyes = ",pyes,"%")