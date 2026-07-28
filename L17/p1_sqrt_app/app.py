from flask import *

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
	if request.method == "POST":
		try:
			num=float(request.form.get("num"))
			if num >= 0:
				sqrt=num**0.5
				msg = "square root of " +str(num)+" = "+str(round(sqrt,2))
				return render_template("home.html",msg=msg)
			else:
				msg="pls enter +ve numbers only"
				return render_template("home.html",msg=msg)
		except ValueError:
			msg="pls enter numbers only"
			return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)