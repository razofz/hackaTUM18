from flask import Flask, render_template, request
import Stations
application = Flask(__name__)
stations_array=[];
stations_array=Stations.getStations()

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
@application.route("/func")
def func():
    return render_template('func.html', page="func")
@application.route("/func")
def stations():

    for station in array:
        stations_array.append(station.name)

    return render_template('func.html', stations=stations_array)

if __name__ == "__main__":
    application.run(host='127.0.0.1')
