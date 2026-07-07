#understand data

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("housingdata.csv")
print(data)

#independent variable / feature / input
x = data["area"]
#dependent variable / target / output
y = data["price"]

plt.figure(figsize=(12,5))
plt.scatter(x,y,color="blue")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Lonavla")
plt.show()