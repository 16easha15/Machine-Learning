#use model

#import lib
from pickle import load

#load the model
with open("heart.pkl","rb") as f:
	model = load(f)
#make prediction
age = int(input("Age "))
sex = int(input("Gender 1=male 0=female "))
cp = int(input("chest pain type from 0 - 3 "))
trtbps = int(input("trtbps in mm hg "))
chol = int(input("cholestrol level in mg/dl "))
fbs = int(input("fbs "))
restecg = int(input("restecg "))
thalachh = int(input("thalachh "))
exng = int(input("exng "))
oldpeak = float(input("oldpeak "))
slp = int(input("slp "))
caa = int(input("caa from 0-3 "))
thall = int(input("thall type 0/1/2/3  "))
 
d=[[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]]
ans = model.predict(d)
print(ans)