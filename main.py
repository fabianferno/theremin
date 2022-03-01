from hcsr04 import HCSR04
from time import sleep

# ESP32
sensor1 = HCSR04(trigger_pin=2, echo_pin=13, echo_timeout_us=1000000)
sensor2 = HCSR04(trigger_pin=14, echo_pin=15, echo_timeout_us=1000000)


# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True: 
    print('Distance:', sensor1.distance_cm(), 'cm', sensor2.distance_cm(),'cm')
    sleep(0.5)