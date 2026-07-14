import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

data = pd.read_csv("age_vehicle.csv")

feature = data[["Age"]]
target = data["Vehicle"]

x_train,x_test,y_train,y_test = train_test_split(feature.values,target)

model = LogisticRegression()
model.fit(x_train,y_train)

print(x_test)
print(y_test)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(y_pred)

cf = confusion_matrix(y_test,y_pred)
print(cf)

cr = classification_report(y_test,y_pred)
print(cr)