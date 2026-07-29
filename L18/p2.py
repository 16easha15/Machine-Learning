from pickle import load

fn="hpp.pkl"
with open(fn,"rb") as f:
	model =load(f)
	print("model ready")
area = float(input("enter area "))
price = model.predict([[area]])
msg = str(round(price[0],2))+" crores"
print(msg)
