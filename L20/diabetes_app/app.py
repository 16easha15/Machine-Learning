from flask import *
from pickle import load

with open("diabetes.pkl","rb") as f:
	model=load(f)
	print("model ready")
	
app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
	if request.method == "POST":
		age = float(request.form.get("age"))
		bmi = float(request.form.get("bmi"))
		fs = float(request.form.get("fs"))
		hb = float(request.form.get("hb"))
		d1 =[age,bmi,fs,hb]
		ge = int(request.form.get("ge"))
		if ge == 1:
			d2=[1,0]
		else:
			d2=[0,1]

		ht = int(request.form.get("ht"))
		if ht == 1:
			d3=[1,0]
		else:
			d3=[0,1]

		fh = int(request.form.get("fh"))
		if fh == 1:
			d4=[1,0]
		else:
			d4=[0,1]
		d=[d1+d2+d3+d4]
		ans = model.predict(d)
		msg = "Our System says " +str(ans[0])+ " we can also make mistakes.pls consult doctor"
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")

if  __name__ == "__main__":
	app.run(debug=True,use_reloader=True)



