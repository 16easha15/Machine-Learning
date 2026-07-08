#model use --> cui app

#import lib
from pickle import load
import os 

#load the model
if os.path.exists("real_estate.pkl"):
	with open("real_estate.pkl","rb") as f:
		model = load(f)
else:
	print("model not found")
	exit()

#make prediction
area = float(input("enter area "))
bedrooms = float(input("enter number of bedrooms "))
price = model.predict([[area,bedrooms]])
print(price)