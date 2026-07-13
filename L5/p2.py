#Cat Data to Numerical Data

import pandas as pd

data = pd.read_csv("scap.csv")

features = data[["state","city","area"]]
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)