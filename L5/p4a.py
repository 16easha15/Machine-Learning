import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

data = pd.read_csv("ps.csv")
feature = data[["Level"]]
target = data["Salary"]

pf = PolynomialFeatures(degree=6)
pfeature = pf.fit_transform(feature.values)
print(feature)
print(pfeature)

model = LinearRegression()
model.fit(pfeature,target)

plt.scatter(data["Level"],data["Salary"],color="red")
plt.plot(data["Level"],model.predict(pf.transform(data[["Level"]])),color="blue")
plt.show()