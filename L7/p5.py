#how to calculate->confusion matrix,classification report and accuracy

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report

data=pd.read_csv("age_sub.csv")
 
feature = data[["age"]]
target = data["sub"]

x_train,x_test,y_train,y_test = train_test_split(feature.values,target,test_size=0.4)
print(x_train)
print(y_train)

print(x_test)
print(y_test)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print(y_pred)

cf = confusion_matrix(y_test,y_pred)
print(cf)

cr = classification_report(y_test,y_pred)
print(cr)