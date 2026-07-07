#model create 

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pickle import dump

data = pd.read_csv("emp_salary.csv")
feature = data[["exp"]]
target = data["sal"]

x_train,x_test,y_train,y_test=train_test_split(feature.values,target)

model=LinearRegression()
model.fit(x_train,y_train)

score = model.score(x_test,y_test)
print(round(score*100,2),"%")

f=open("salary.pkl","wb")
dump(model,f)
f.close()
print("model created")