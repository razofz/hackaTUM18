from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def landing():
	return render_template('index.html', page="home")

@application.route("/yousave")
def kontakt():
	return render_template('yousave.html', page="yousave")

if __name__ == "__main__":
	application.run(host='0.0.0.0')

