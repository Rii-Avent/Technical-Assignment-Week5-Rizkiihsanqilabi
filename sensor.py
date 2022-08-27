import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
current_hummidity = 0
current_temperatre = 0
def sensor_dht11():
 while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None:
        current_hummidity = humidity
    if temperature is not None:
        current_temperatre = temperature
        
        
    print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(current_temperatre, current_hummidity))
        
    
        
        
    time.sleep(10);
    
sensor_dht11()
    

