#Cat Data to Numerical Data using OneHotEncoder

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("scap.csv")
print(data)

#categorical columns
cfeatures = data[["state","city"]]
print(cfeatures)

#numerical column
nfeatures = data[["area"]]
print(nfeatures)

#create encoder
ohe = OneHotEncoder(sparse_output=False)

#encode categorical data
ecfeatures = ohe.fit_transform(cfeatures)
print(ecfeatures)

#convert encoded data to dataframe
ecfeatures = pd.DataFrame(
	ecfeatures,
	columns=ohe.get_feature_names_out(cfeatures.columns)	
)
print(ecfeatures)

#combine encoded columns with numerical column
final_features = pd.concat([nfeatures,ecfeatures ],axis=1)
print(final_features)