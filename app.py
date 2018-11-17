from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def landing():
    avg_saved_per_month = 35
    return render_template('index.html', avg_saved=avg_saved_per_month)

@application.route("/yousave")
def yousave():
    return render_template('yousave.html', page="yousave")

if __name__ == "__main__":
    application.run(host='127.0.0.1')
