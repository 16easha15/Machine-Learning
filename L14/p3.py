#import lib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

#load the data
data = pd.read_csv("salary.csv");
print(data)

#feature and target
feature = data[["Level"]]
target = data["Salary"]

#model
model = RandomForestRegressor(n_estimators=10)
model.fit(feature.values,target)

#prediction
level = int(input("Enter level "))
ans=model.predict([[level]])
print(ans)