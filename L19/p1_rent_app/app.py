from flask import *
from pickle import load

with open("rent.pkl","rb") as f:
	model=load(f)
	print("model ready")

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
	if request.method =="POST":
		bhk = float(request.form.get("bhk"))
		size = float(request.form.get("size"))	
		bath = float(request.form.get("bath"))
		fur = int(request.form.get("fur"))
		if fur == 1:
			d=[[bhk,size,bath,1,0,0]]
		elif fur == 2:
			d=[[bhk,size,bath,0,1,0]]
		else:
			d=[[bhk,size,bath,0,0,1]]
		ans = model.predict(d)
		msg = "Estimated Rent = "+str(round(ans[0],2))
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")
if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)
	
			