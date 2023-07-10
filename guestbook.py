from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.secret_key = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

db = SQLAlchemy(app) 

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))

@app.route("/")
def home():
	results = Comments.query.all()

	return render_template("index.html", result = results)

@app.route("/sign")
def sign():
	return render_template("sign.html")

@app.route("/process", methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['cmnt']

	sign = Comments(name=name, comment=comment)
	db.session.add(sign)
	db.session.commit()

	return redirect(url_for("home"))

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)	