import json
import methods
from time import sleep, strftime, gmtime

from models import consumption

numeroSalle = "2"
titleSalle = "temperature"

methods.mySub(methods.salle())

i = 0
while i < 20:
    consumption.data["PAPP"] = methods.getConsumption()
    MQTT_MSG = json.dumps(consumption.data)
    methods.myPubOnTest(methods.salle(), MQTT_MSG)
    i += 1
    sleep(2)

methods.disconnecting()



#mosquitto_sub -h test.mosquitto.org -p 1883 -t EPSI/B3A/leoH/salle1/temperature

