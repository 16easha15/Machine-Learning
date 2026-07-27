from flask import *
from datetime import *

app = Flask(__name__)

@app.route("/")
def home():
	dt = datetime.now()
	hr = dt.hour
	if hr < 12:
		msg = "Good Morning"
	elif hr < 16:
		msg = "Good Afternoon"
	else:
		msg = "Good Evening"
	return render_template("home.html",msg=msg)
app.run(debug=True,use_reloader=True)