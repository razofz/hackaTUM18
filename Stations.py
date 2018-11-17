import csv

class Car:

    def __init__(self, type, fuelConsume, gasperkm, carPrice, insurancePrice):
        self.type = type
        self.fuelconsume = fuelConsume
        self.gasperkm = gasperkm
        self.carPrice = carPrice
        self.insurancePrice = insurancePrice



class Stations:
    def __init__(self, name, latitude, longitude, ring):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.ring = ring

