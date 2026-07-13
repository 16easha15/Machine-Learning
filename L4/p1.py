#data visualization

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("aqp_july26.csv")
print(data)

x = data["qty"]
y = data["price"]

plt.scatter(x,y)
plt.xlabel("qty")
plt.ylabel("price")
plt.title("Apple")
plt.show()