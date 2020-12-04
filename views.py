from flask import *
#from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql7.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql7380110'
app.config['MYSQL_PASSWORD'] = '2mLlmiHYs8'
app.config['MYSQL_DB'] = 'sql7380110'

mysql = MySQL(app)

def requestSQL(command, args):
	try:
		cur = mysql.connection.cursor()
		print("Connection success")
		cur.execute(command, args)
		print("Execution success")
		mysql.connection.commit()
		print("Commit success")
		cur.close()
	except:
		return 'Error'
	return "Ok"


def requestForm(request):
	city = request.form.get("city")
	spot = request.form.get("spot")
	name = request.form.get("name")
	date = request.form.get("date")
	times = request.form.get("times")
	timee = request.form.get("timee")
	return requestSQL('''INSERT INTO session(waterman, city, spot, date, time, timeEnd) VALUES(%s, %s, %s, %s, %s)''', (name, city, spot, date, times, timee))

def requestFrequentations(request):
	swimmers = request.form.get("swimmers")
	pan = request.form.get("pan")
	fishing = request.form.get("fishing")
	entertainment = request.form.get("entertainment")
	sailing = request.form.get("sailing")

@app.route('/',methods=["GET"])
def home():
	return render_template("form.html")


@app.route('/form/', methods=["GET","POST"])
def form():
	if request.method == "POST":
		pass
	return render_template("form.html")


@app.route('/frequentation/', methods=["GET", "POST"])
def frequentation():
	if request.method == "POST":
		return requestForm(request)

	return render_template("frequentation.html")




@app.route('/waterman/',methods=["GET","POST"])
def waterman():
	if request.method=="POST":
		solcream=request.form.get("solcream")
		perfume=request.form.get("perfume")
		hydracream=request.form.get("hydracream")
		makeup=request.form.get("makeup")
		petrol=request.form.get("petrol")
		cigar=request.form.get("cigar")
		fertilizer=request.form.get("fertilizer")
		paints=request.form.get("paints")
		others=request.form.get("others")
	return render_template("waterman.html")


@app.route('/merci/',methods=["GET"])
def merci():
	return render_template("merci.html")

if __name__ == "__main__":
	app.run()
