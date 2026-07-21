#import lib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

#load the data
data = pd.read_csv("loan.csv")
print(data)

#features and target
features = data[["GENDER","OCCUPATION"]]
target = data["DEFAULT"]

#model
model = make_pipeline(
		OneHotEncoder(),
		DecisionTreeClassifier()
	);
model.fit(features.values,target)

plt.figure(figsize=(12,5))
tree = model.named_steps["decisiontreeclassifier"]
plot_tree(tree,fontsize=12,filled=True,feature_names=["gender_female","gender_male","occ_business","occ_salary"],class_names=["loan de do","loan mat do"])
plt.show()