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
		cur.execute(command, args)
		mysql.connection.commit()
		cur.close()
	except:
		return 'Error'
	return "Ok"



@app.route('/')
def index():
	return render_template("index.html")


if __name__ == "__main__":
	app.run()
