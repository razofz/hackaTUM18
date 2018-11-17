from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
def landing():
    avg_saved_per_month = 35
    return render_template('index.html', avg_saved=avg_saved_per_month)

@application.route("/personalised", methods=['GET', 'POST'])
def personalised():
    if request.method == 'GET':
        return render_template('personalised.html', post=False)
    else:
        # car.getMonthlyValue()

        return render_template('personalised.html', car_monthly=request.form['from'], 
                public_transport_monthly=request.form['dropdowncars'], post=True)

if __name__ == "__main__":
    application.run(host='127.0.0.1')
