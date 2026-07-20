#import lib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

#load the data
data = pd.read_csv("lung_cancer.csv")
print(data)

#check and handle null data
print(data.isnull().sum())
print(data.info())

#features and target
features = data.drop(["LUNG_CANCER"],axis="columns")
target = data["LUNG_CANCER"]

#handle categorical data
nfeatures = pd.get_dummies(features)
print(nfeatures)

#feature scaling
mms = MinMaxScaler()
sfeatures = mms.fit_transform(nfeatures.values)
print(sfeatures)

sf = pd.DataFrame(sfeatures)
sf.to_csv("sf.csv")

#train and test
x_train,x_test,y_train,y_test = train_test_split(sfeatures,target)

#find k
k = int(len(data)**0.5)
if k % 2 == 0 :
	k = k + 1

#model
model = KNeighborsClassifier(n_neighbors=k,metric="euclidean")
model.fit(x_train,y_train)

#check for balance/imbalance
print(data["LUNG_CANCER"].value_counts())

#classification report
y_pred = model.predict(x_test)
cr = classification_report(y_test,y_pred)
print(cr)

#prediction
d = [[0.8030303030303032,1.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,1.0]]
sd = mms.transform(d)
ans = model.predict(sd)
print(ans)