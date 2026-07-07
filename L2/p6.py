#model use

from pickle import load

f=open("salary.pkl","rb")
model = load(f)
f.close()

exp=float(input("enter exp "))
salary = model.predict([[exp]])
print(salary)