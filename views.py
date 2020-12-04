from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql7.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql7380110'
app.config['MYSQL_PASSWORD'] = '2mLlmiHYs8'
app.config['MYSQL_DB'] = 'sql7380110'

mysql = MySQL(app)

def getRequestSQL(command):
	try:
		cur = mysql.connection.cursor()
		print("Connection success")
		cur.execute(command)
		print("Execution success")
		rows = cur.fetchall()
		return rows
	except:
		return None


def requestSQL(command, args):
	try:
		cur = mysql.connection.cursor()
		print("Connection success")
		cur.execute(command, args)
		print("Execution success")
		mysql.connection.commit()
		print("Commit success")
	except:
		return 1
	return 0


def requestForm(request):
	# Session
	city = request.form.get("city")
	spot = request.form.get("spot")
	name = request.form.get("name")
	date = request.form.get("date")
	times = request.form.get("times")
	timee = request.form.get("timee")

	# Frequentations
	swimmers = request.form.get("swimmers")
	pan = request.form.get("pan")
	fishing = request.form.get("fishing")
	entertainment = request.form.get("entertainment")
	sailing = request.form.get("sailing")

	# Products
	solcream = request.form.get("solcream")
	perfume = request.form.get("perfume")
	hydracream = request.form.get("hydracream")
	makeup = request.form.get("makeup")
	petrol = request.form.get("petrol")
	cigar = request.form.get("cigar")
	fertilizer = request.form.get("fertilizer")
	paints = request.form.get("paints")
	others = request.form.get("others")

	return requestSQL('''INSERT INTO session(waterman, city, spot, date, time, timeEnd) VALUES(%s, %s, %s, %s, %s, %s)''', (name, city, spot, date, times, timee))

@app.route('/afficher_stats/')
def stats():
	rows = getRequestSQL('select * from session;')
	print(rows)
	return render_template("afficher_stats.html", list=rows)

@app.route('/', methods=["GET"])
def home():
	return render_template("home.html")


@app.route('/form/', methods=["GET", "POST"])
def form():
	return render_template("form.html")

@app.route('/form_en/', methods=["GET", "POST"])
def form():
	return render_template("form_en.html")


@app.route('/merci/', methods=["GET", "POST"])
def merci():
	if request.method == "POST":
		status = requestForm(request)

	return render_template("merci.html")

@app.route('/thanks/', methods=["GET","POST"])
def thanks():
	if request.method == "POST":
		status = requestForm(request)

	return render_template("thanks.html")






if __name__ == "__main__":
	app.run()
