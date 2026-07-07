#how does model make prediction

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("housingdata.csv")
feature = data[["area"]]
target = data["price"]

model = LinearRegression()
model.fit(feature.values,target)

plt.figure(figsize=(12,5))
plt.scatter(data["area"],data["price"],color="blue")
plt.plot(data["area"],model.predict(data[["area"]]),color="red")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Lonavla")

plt.show()

