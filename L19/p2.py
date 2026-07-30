#import lib
from pickle import load

#restore the model
with open("rent.pkl","rb") as f:
	model = load(f)
	print("model ready")

#prediction
bhk=float(input("enter bhk "))
size=float(input("enter size in square feet "))
bath =float(input("enter number of bathrooms "))
fur = int(input("1. furnished,2. semi-furnished and 3. unfurnished "))
if fur == 1:
	d=[[bhk,size,bath,1,0,0]]
elif fur == 2:
	d=[[bhk,size,bath,0,1,0]]
else:
	d=[[bhk,size,bath,0,0,1]]
ans = model.predict(d)
msg = "Estimated Rent = "+str(round(ans[0],2))
print(msg)