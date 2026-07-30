from flask import *
from pickle import *

with open("car.pkl","rb") as f:
	model=load(f)
	print("model ready")

with open("mms.pkl","rb") as f:
	mms=load(f)
	print("mms ready")
	
app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
	if request.method == "POST":
		age = float(request.form.get("age"))
		kms = float(request.form.get("kms"))
		name = int(request.form.get("name"))
		if name == 1:
			d = [[age,kms,1,0,0]]
		elif name == 2:
			d = [[age,kms,0,1,0]]
		else:
			d = [[age,kms,0,0,1]]
		sd = mms.transform(d)
		ans=model.predict(sd)
		msg = "Estimated Used Car Price  = "+str(round(ans[0],2))
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")

if  __name__ == "__main__":
	app.run(debug=True,use_reloader=True)



