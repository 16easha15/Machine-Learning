#import lib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier

#load the data
data = pd.read_csv("run.csv")
print(data)

#features and target
features = data[["Weather","Just Ate"]]
target = data["Will I Go Running?"]

#model
model = make_pipeline(
	OneHotEncoder(),
	DecisionTreeClassifier()
	)
model.fit(features.values,target)

#prediction
we = input("Weather:Sunny/Rainy ")
ate = input("Just Ate:yes/no ")
d = pd.DataFrame([[we,ate]])
ans = model.predict(d)
print(ans)