from pickle import load

with open("car.pkl","rb") as f:
	model=load(f)
	print("model ready")

with open("mms.pkl","rb")  as f:
	mms=load(f)
	print("mms ready")

age =float(input("enter age "))
kms = float(input("enter kms "))
name = int(input("1 for Mahindra , 2 for Maruti and 3 for Tata "))
if name == 1:
	d = [[age,kms,1,0,0]]
elif name == 2:
	d = [[age,kms,0,1,0]]
else:
	d = [[age,kms,0,0,1]]

sd = mms.transform(d)
ans=model.predict(sd)
print(ans)

		
