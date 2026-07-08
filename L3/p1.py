#import lib
import pandas as pd
from sklearn.linear_model import LinearRegression

#load the data
data = pd.read_csv("abpj_july26.csv")
print(data)

#feature and target
features = data[["area","bedrooms"]]
target = data["price"]

#model
model = LinearRegression()
model.fit(features.values,target)

#predict
area = float(input("enter area "))
bedrooms = float(input("enter number of bedrooms "))
price = model.predict([[area,bedrooms]])
print(price)