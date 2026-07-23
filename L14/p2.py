#import lib
import pandas as pd
from sklearn.tree import DecisionTreeRegressor,plot_tree
import matplotlib.pyplot as plt

#load the data
data = pd.read_csv("salary.csv");
print(data)

#feature and target
feature = data[["Level"]]
target = data["Salary"]

#model
model = DecisionTreeRegressor()
mf=model.fit(feature.values,target)

#prediction
level = int(input("Enter level "))
ans=model.predict([[level]])
print(ans)

plt.figure(figsize=(12,5))
plot_tree(mf,filled=True,feature_names=["level"])
plt.show()