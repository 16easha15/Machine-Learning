#import lib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#load the data
data = pd.read_csv("es_july26.csv")
print(data)

#perform eda
sns.histplot(data["Experience (years)"],kde=True)
plt.show()
sns.histplot(data["Salary (thousands of dollars)"],kde=True)
plt.show()

#handle missing data
data.fillna({
	"Experience (years)" : data["Experience (years)"].mean(),
	"Salary (thousands of dollars)" :data["Salary (thousands of dollars)"].median()},inplace=True)
print(data.isnull().sum())

#feature and target
feature = data[["Experience (years)"]]
target = data["Salary (thousands of dollars)"]

#train and test
x_train,x_test,y_train,y_test = train_test_split(feature.values,target)

#model
model = LinearRegression()
model.fit(x_train,y_train)

#score
score = model.score(x_test,y_test)
print(score)

#predict
exp = float(input("enter exp in year "))
salary = model.predict([[exp]])
print(salary)
