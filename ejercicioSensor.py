import time as sleep
import Adafruit_DHT as dht 
import RPi.GPIO as gpio 
gpio.setmode(gpio.BCM)

def DHT11_data():
    humi, temp = dht.read_retry(dht.DHT11, 18)
    return humi, temp
while True:
    try:
        humedad, temperatura=DHT11_data()
        if humedad is not None and temperatura is not None:
            print("Humedad: ", humedad, " temperatura:", temperatura)
        else:
            print("Error en la lectura del sensor")
            