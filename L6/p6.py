import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

data=pd.read_csv("hours_result.csv")

feature=data[["hours"]]
target=data["result"]

x_train,x_test,y_train,y_test=train_test_split(feature.values,target,test_size=0.2)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(x_test)
print(y_test)
print(y_pred)

cm = confusion_matrix(y_test,y_pred)
print(cm)

cr = classification_report(y_test,y_pred)#diff between actual values and predicted
print(cr)
