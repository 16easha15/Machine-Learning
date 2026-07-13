#find missing data
import pandas as pd
data = pd.read_csv("aqp_july26.csv")
print(data.isnull())
print(data.isnull().sum())