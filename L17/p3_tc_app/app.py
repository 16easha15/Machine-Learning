from flask import  *

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
	if request.method == "POST":
		temp=float(request.form.get("temp"))
		choice = request.form.get("choice")
		if choice == "c2f":
			ans = (temp*1.8)+32
			msg=str(temp)+ " in cel= "+str(ans)+" in fah"
		else:
			ans = (temp-32)/1.8
			msg=str(temp)+ " in fah = "+str(ans)+" in cel"
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)