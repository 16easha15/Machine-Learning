import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("hours_result.csv")
data.sort_values(by="hours",inplace=True)
print(data)

feature=data[["hours"]]
target =data["result"]

model=LogisticRegression()
model.fit(feature.values,target)

x=data["hours"]
y=data["result"]
plt.scatter(x,y,color="red")
plt.plot(x,model.predict(feature.values),color="blue")
plt.show()