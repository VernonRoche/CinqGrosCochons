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

@app.route('/frequentation/',methods=["GET","POST"])
def frequentation():
	if request.method=="POST":
		swimmers=request.form.get("swimmers")
		pan=request.form.get("pan")
		fishing=request.form.get("fishing")
		entertainment=request.form.get("entertainment")
		sailing=request.form.get("sailing")
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

if __name__ == "__main__":
	app.run()
