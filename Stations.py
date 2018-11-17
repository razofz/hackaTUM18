import csv

class Car:

    def __init__(self, type, fuelConsume, gasperkm, carPrice, insurancePrice):
        self.type = type
        self.fuelconsume = fuelConsume
        self.gasperkm = gasperkm
        self.carPrice = carPrice
        self.insurancePrice = insurancePrice

class Station:
    def __init__(self, name, longitude, latitude, ring):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.ring = ring

#get the distance between stations (KM)
def getStationsDistance(station1, station2):
    #xDif = abs(station1.latitude - station2.latitude)
    #yDif = abs(station1.longitude - station2.longitude)

    R = 6373.0

    lat1 = radians(station1.latitude)
    lon1 = radians(station1.longitude)
    lat2 = radians(station2.latitude)
    lon2 = radians(station2.longitude)

    dlon = abs(lon2 - lon1)
    dlat = abs(lat2 - lat1)

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    #print("Result:", distance)
    return distance

#get Monthly ticket price of 2 different stations
def getMonthlyPrice(station1, station2):
    array = [55.20, 66.60, 79.10, 90.40, 103.70, 116.50, 127.80, 140.50, 152.50, 163.40, 175.10, 188.00, 201.30, 212.50, 225.60]

    if (abs(station1.ring - station2.ring) == 0):
       return array[0]
    else:
        return array[abs(station1.ring - station2.ring)-1]

