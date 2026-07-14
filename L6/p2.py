import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hours_result.csv")
print(data)

x = data["hours"]
y = data["result"]

plt.scatter(x,y,color="red")
plt.show()