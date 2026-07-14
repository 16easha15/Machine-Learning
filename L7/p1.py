#reg vs clf
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("age_sub.csv")
print(data)

plt.scatter(data["age"],data["sub"],color="red")
plt.show()
