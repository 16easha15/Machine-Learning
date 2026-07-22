#import lib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#load the data
data = pd.read_csv("run.csv")
print(data)

#features and target
features = data[["Weather","Just Ate"]]
target = data["Will I Go Running?"]

#handle cat data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#model
model = RandomForestClassifier(n_estimators=10)
model.fit(nfeatures.values,target)

#prediction
we = int(input("Weather : 1 for Rainy and 2 for Sunny "))
ate = int(input("Ate: 1 for no and 2 for yes "))
if we == 1:
	d1 = [1,0]
else:
	d1 = [0,1]
if ate == 1:
	d2 = [1,0]
else:
	d2 = [0,1]
d = [d1+d2]
ans = model.predict(d)
print(ans)