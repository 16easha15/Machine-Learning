from flask import *
from sqlite3 import *
DB_NAME ="bungalow_price.db"

def db_setup():
	con=None
	try:	
		con=connect(DB_NAME)
		sql="create table if not exists bungalow(location text,area float,price float)"
		cursor = con.cursor()
		cursor.execute(sql)
		con.commit()
		print("done")
	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()
db_setup()

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
	if request.method == "POST":
		location=request.form.get("location")
		area=float(request.form.get("area"))
		price=float(request.form.get("price"))
		con=None
		try:
			con=connect(DB_NAME)
			sql="insert into bungalow values(?,?,?)"
			cursor = con.cursor()
			cursor.execute(sql,(location,area,price))
			con.commit()
			msg="record saved"
			return render_template("home.html",msg=msg)
		except Exception as e:
			print("issue",e)
			msg="issue"+str(e)	
			return render_template("home.html",msg=msg)
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)