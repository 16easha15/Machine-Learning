from flask import *

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
	if request.method =="POST":
		num = int(request.form.get("num"))
		if num % 2 == 0:
			msg = str(num) + " is even"
		else:
			msg = str(num) + " is odd"
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")
app.run(debug=True,use_reloader=True)

