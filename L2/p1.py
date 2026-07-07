import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("emp_salary.csv")
print(data)

x = data["exp"]
y = data["sal"]

plt.scatter(x,y,color="red")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()