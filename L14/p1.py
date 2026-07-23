#import lib
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

#load the data
data = pd.read_csv("salary.csv");
print(data)

#feature and target
feature = data[["Level"]]
target = data["Salary"]

#model
model = DecisionTreeRegressor()
model.fit(feature.values,target)

#prediction
level = int(input("Enter level "))
ans=model.predict([[level]])
print(ans)