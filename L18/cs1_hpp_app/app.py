from flask import *
from pickle import load
import os

fn="hpp.pkl"

if os.path.exists(fn):
	with open(fn,"rb") as f:
		model = load(f)
else:
	print(fn,"not found")

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
	if request.method=="POST":
		area=float(request.form.get("area"))
		price=model.predict([[area]])
		msg = str(round(price[0],2))+" crores"
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")

if __name__ == "__main__":	
	app.run(debug=True,use_reloader=True)