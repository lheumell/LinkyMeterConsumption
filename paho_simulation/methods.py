from random import uniform
from connection import client


def mySub(salle):
    print('vous etes rentré dans la salle : ' + salle)
    client.subscribe(salle)


def myPubOnTest(salle, MSG):
    client.publish(salle, MSG)


def getConsumption():
    return 00 + round(uniform(300, 400), 0)


def salle():
    return 'EPSI/B3A/leoH/IOT/consumption'


def disconnecting():
    client.disconnect();
    print("Fin du programme")
