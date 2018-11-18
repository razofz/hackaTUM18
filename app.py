from flask import Flask, render_template, request
from stations import getStations, Car, getStationsDistance, getMonthlyPriceTransportation, getDailyPrice, getStation, getCar
application = Flask(__name__)

array = []
stations_array=getStations()

@application.route("/")
def landing():
    avg_saved_per_month = 52
    return render_template('index.html', avg_saved=avg_saved_per_month)

@application.route("/personalised", methods=['GET', 'POST'])
def personalised():
    if len(array) == 0:
        for station in stations_array:
            array.append(station.name)
    

    if request.method == 'GET':
        return render_template('personalised.html', post=False, stations=array)
    else:
        print(request.form['dropdowncars'])
        car = getCar(request.form['dropdowncars'])
        print(type(car))

        fromStation = getStation(request.form['from'])
        toStation = getStation(request.form['to'])
        distance = getStationsDistance(fromStation, toStation)

        return render_template('personalised.html', 
            car_monthly=(car.getMonthlyPriceGas(distance)+car.getMonthlyLossofValue(distance)), 
            car_daily=(car.getDailyPriceGas(distance)+car.getDailyLossofValue(distance)), 
            public_transport_monthly=getMonthlyPriceTransportation(fromStation, toStation), 
            public_transport_daily=getDailyPrice(fromStation, toStation), 
            post=True, stations=array)

if __name__ == "__main__":
    application.run(host='127.0.0.1')
