#import lib
import pandas as pd
from sklearn.linear_model import LinearRegression

#load the data
data = pd.read_csv("abpj_july26.csv")
print(data)

#features and target
features = data[["area","bedrooms"]]
target = data["price"]

#model
model = LinearRegression()
model.fit(features.values,target)

#predict
b0=model.intercept_
b1=model.coef_[0]
b2=model.coef_[1]
print("b0 = ",b0)
print("b1 = ",b1)
print("b2 = ",b2)
