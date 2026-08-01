from pickle import load

with open("diabetes.pkl","rb") as f:
	model = load(f)
	print("model ready")

age =float(input("enter age "))
bmi = float(input("enter bmi "))
fs =float(input("enter fasting sugar "))
hb = float(input("enter hba1c "))
d1 = [age,bmi,fs,hb]

ge = int(input("1 for female and 2 for male"))
if ge == 1:
	d2=[1,0]
else:
	d2=[0,1]

ht = int(input("Hypertension: 1 for no and 2 for yes"))
if ht == 1:
	d3=[1,0]
else:
	d3=[0,1]

fh = int(input("Family History: 1 for no and 2 for yes"))
if fh == 1:
	d4=[1,0]
else:
	d4=[0,1]
d=[d1+d2+d3+d4]
ans = model.predict(d)
print(ans[0])