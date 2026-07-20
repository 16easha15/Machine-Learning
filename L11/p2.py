#import lib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer

#load the data
data = pd.read_csv("lung_cancer.csv")
print(data)

#check and handle null data
print(data.isnull().sum())
print(data.info())

#features and target
features = data.drop(["LUNG_CANCER"],axis="columns")
target = data["LUNG_CANCER"]

#train and test
x_train,x_test,y_train,y_test = train_test_split(features,target)

#find k
k = int(len(data)**0.5)
if k % 2 == 0 :
	k = k + 1

#find the names of cat and num columns
cat_cols = ["GENDER"]
print(cat_cols)
num_cols = features.drop("GENDER",axis=1).columns

#create CT
ct = ColumnTransformer([
	("cat",OneHotEncoder(sparse_output=False),cat_cols),
	("num",MinMaxScaler(),num_cols)
	])


#model
model = make_pipeline(
		ct,
		KNeighborsClassifier(n_neighbors=k,metric="euclidean")
	)
model.fit(x_train,y_train)

#check for balance/imbalance
print(data["LUNG_CANCER"].value_counts())

#classification report
y_pred = model.predict(x_test)
cr = classification_report(y_test,y_pred)
print(cr)

#prediction
d =pd.DataFrame([{
	"GENDER":"M",
	"AGE":69,
	"SMOKING":1,
	"YELLOW_FINGERS":2,
	"ANXIETY":2,
	"PEER_PRESSURE":1,
	"CHRONIC DISEASE":1,
	"FATIGUE ":2,
	"ALLERGY ":1,
	"WHEEZING":2,
	"ALCOHOL CONSUMING":2,
	"COUGHING":2,
	"SHORTNESS OF BREATH":2,
	"SWALLOWING DIFFICULTY":2,
	"CHEST PAIN":2
	}])
ans = model.predict(d)
print(ans)