import sqlite3

import paho.mqtt.client as mqtt
import json

from connection_db import sinfun


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("EPSI/B3A/leoH/IOT/consumption")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    obj = json.loads(msg.payload)
    myADCO = obj["ADCO"]
    myOPTARIF = obj["OPTARIF"]
    myISOUSC = obj["ISOUSC"]
    myBASE = obj["BASE"]
    myPTEC = obj["PTEC"]
    myINST = obj["INST"]
    myMAX = obj["MAX"]
    myPAPP = obj["PAPP"]
    myHHPHC = obj["HHPHC"]
    myMOTDETAT = obj["MOTDETAT"]



    print('insert')
    print(myPAPP)
    data = []
    data.append({'ADCO': myADCO, 'OPTARIF': myOPTARIF, 'ISOUSC': myISOUSC, 'BASE': myBASE, 'PTEC': myPTEC, 'INST': myINST, 'MAX' : myMAX, 'PAPP': myPAPP, 'HHPHC': myHHPHC, 'MOTDETAT': myMOTDETAT})
    # the list of records is written to the database in one go:
    sinfun.insert_many(data)
    print('done')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
