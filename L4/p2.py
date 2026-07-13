#solution using LR
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("aqp_july26.csv")
feature = data[["qty"]]
target = data["price"]

model = LinearRegression()
model.fit(feature.values,target)