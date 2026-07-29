#model create 

#import lib 
import pandas as pd
from sklearn.linear_model import LinearRegression
from pickle import dump

#load the data
data = pd.read_csv("cs1.csv")
print(data)

#features and target
features = data[["area in square feet"]]
target = data["price (in crores)"]

#model creation
model = LinearRegression()
model.fit(features.values,target)

#dump the file 
with open("hpp.pkl","wb") as f:
	dump(model,f)
	print("model saved")
