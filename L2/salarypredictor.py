from tkinter import *
from pickle import load
import os

root = Tk()
root.title("Salary Predictor App")
root.geometry("600x400+300+30")
f = ("Arial",30,"bold")

def find():
	try:
		exp = float(ent_exp.get())
		if exp <= 0:
			msg = "exp should not be less than 1"
			lab_msg.configure(text=msg,fg="red")
			return
	
		fn = "salary.pkl"
		if os.path.exists(fn):
			with open(fn,"rb") as f:
				model = load(f)
			
			salary = model.predict([[exp]])
			msg = "Estimated Salary = "+str(round(salary[0],2))
			lab_msg.configure(text=msg,fg="red")
		else:
			msg="model not found"
			lab_msg.configure(text=msg,fg="red")
	except ValueError:
		msg="invalid salary"
		lab_msg.configure(text=msg,fg="red")
 
lab_exp = Label(root,text="Enter Exp in Years",font=f)
ent_exp = Entry(root,font=f,bd=2)
btn_find = Button(root,text="Predict Salary",font=f,command=find)
lab_msg = Label(root,text="",font=f)

lab_exp.pack(pady=10)
ent_exp.pack(pady=10)
btn_find.pack(pady=10)
lab_msg.pack(pady=10)


root.mainloop()