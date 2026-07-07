#solve the problem

import pandas as pd 
from sklearn.linear_model import LinearRegression

data = pd.read_csv("housingdata.csv")

feature = data[["area"]]
target = data["price"]

model = LinearRegression()
model.fit(feature.values,target)

area = float(input("Enter Area "))
price = model.predict([[area]])
print("price = ",price)


#pip install pandas
#pip install matplotlib
#pip install scikit-learn