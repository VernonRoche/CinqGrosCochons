from flask import *

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
	if request.method=="POST":
		city=request.form.get("city")
		spot=request.form.get("spot")
		name=request.form.get("name")
		date=request.form.get("date")
		times=request.form.get("times")
		timee=request.form.get("timee")
		print(city+" "+spot)

	return render_template("index.html")


if __name__ == "__main__":
	app.run()
