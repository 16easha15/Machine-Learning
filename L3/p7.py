from tkinter import *
from pickle import load
import os

root = Tk()
root.title("Business Profit Estimator")
root.geometry("600x600+300+30")
f = ("Cambria",30,"bold")

def find():
	try:
		rnd=float(ent_rnd.get())
		admin=float(ent_admin.get())
		ms=float(ent_ms.get())
		fn="bpe.pkl"
		if os.path.exists(fn):
			with open(fn,"rb") as f:
				model = load(f)
			profit=model.predict([[rnd,admin,ms]])
			msg="Profit "+str(round(profit[0],2))
			lab_msg.configure(text=msg,fg="blue")
		else:
			msg="model not found"
			lab_msg.configure(text=msg,fg="red")
	except ValueError:
		msg = "Invalid Input"
		lab_msg.configure(text=msg,fg="red")

lab_rnd = Label(root,text="Enter R&D Spend",font=f)
ent_rnd = Entry(root,font=f)
lab_admin = Label(root,text="Enter Admin Spend",font=f)
ent_admin = Entry(root,font=f)
lab_ms = Label(root,text="Enter Marketing Spend",font=f)
ent_ms = Entry(root,font=f)
btn_profit = Button(root,text="Estimated Profit",font=f,command=find)
lab_msg = Label(root,text="",font=f)

lab_rnd.pack(pady=5)
ent_rnd.pack(pady=5)
lab_admin.pack(pady=5)
ent_admin.pack(pady=5)
lab_ms.pack(pady=5)
ent_ms.pack(pady=5)
btn_profit.pack(pady=5)
lab_msg.pack(pady=5)
root.mainloop()