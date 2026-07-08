#model create

#import lib
import pandas as pd
from sklearn.linear_model import LinearRegression
from pickle import dump

#load the data
data = pd.read_csv("abpj_july26.csv")

#features and target
features = data[["area","bedrooms"]]
target = data["price"]

#model
model = LinearRegression()
model.fit(features.values,target)

#model create
with open("real_estate.pkl","wb") as f:
	dump(model,f)
	print("model creation done")
