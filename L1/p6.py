#import lin
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#load the data
data = pd.read_csv("housingdata.csv")

#feature and target
feature = data[["area"]]
target = data["price"]

#train and test
x_train,x_test,y_train,y_test=train_test_split(feature.values,target,random_state=2)

#model
model = LinearRegression()
model.fit(x_train,y_train)

#score
print(round(model.score(x_test,y_test)*100,2),"%")

#predict
area = float(input("enter area "))
price = model.predict([[area]])
print(round(price[0],2),"crs") 