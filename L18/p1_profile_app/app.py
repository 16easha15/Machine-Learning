from flask import * 
from sqlite3 import *

def db_setup():
	con = None
	try:
		con=connect("profile.db")
		sql="create table if not exists student(id integer primary key autoincrement,name text,phone int,gender text,languages text)"
		cursor = con.cursor()
		con.execute(sql)
		con.commit()
		print("done")	
	except Exception as e:
		con.rollback()
		print("issue",str(e))
	finally:
		if con != None:
			con.close()
db_setup()

app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
	if request.method=="POST":
		name = request.form.get("name")
		phone= request.form.get("phone")
		gender=request.form.get("gender")
		languages=""
		if "py" in request.form:
			languages+="Python"
		if "py" in request.form:
			languages+="Java"
		if "py" in request.form:
			languages+="JavaScript"
		con=None
		try:
			con=connect("profile.db")
			sql="insert into student(name,phone,gender,languages) values(?,?,?,?)"
			cursor = con.cursor()
			con.execute(sql,(name,phone,gender,languages))
			con.commit()
			print("done")
			msg="saved"
			return render_template("home.html",msg=msg)
		except Exception as e:
			msg="issue",str(e)
			return render_template("home.html",msg=msg)
		finally:
			if con!=None:
				con.close()
	else:
		return render_template("home.html")

if __name__ =="__main__":
	app.run(debug=True,use_reloader=True)























