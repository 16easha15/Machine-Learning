#import lib
import pandas as pd
from sklearn.naive_bayes import BernoulliNB

#load the data
data = pd.read_csv("email_spam.csv")
print(data)

#feature and target
features = data.drop("spam",axis="columns")
target = data["spam"]

#model
model = BernoulliNB()
model.fit(features.values,target)

#prediction
free = int(input("free ->0 if not present and 1 if present "))
win = int(input("win->0 if not present and 1 if present  "))
offer = int(input("offer->0 if not present and 1 if present  "))
buy = int(input("buy->0 if not present and 1 if present  " ))

spam = model.predict([[free] + [win] + [offer] + [buy]]
)
print(spam)
