import pandas as pd

data = pd.read_csv("aqp_july26.csv")
data.fillna({"price":data["price"].median()},inplace=True)
print(data)