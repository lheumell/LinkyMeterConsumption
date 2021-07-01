from LinkyMeterConsumption.mongoDB.connection_db import sinfun


def getConsumption():
    return sinfun.find_one()
