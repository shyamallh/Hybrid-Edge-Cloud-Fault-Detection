import time
import random
import json

# Sample sensor integration code for Raspberry Pi project
# Replace random values with actual sensor readings when hardware is connected

def read_mpu6050():
    vibration = round(random.uniform(0.1, 3.0), 2)
    return vibration

def read_dht22():
    temperature = round(random.uniform(25.0, 40.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    return temperature, humidity

def read_acs712():
    current = round(random.uniform(0.2, 5.0), 2)
    return current

while True:
    vibration = read_mpu6050()
    temperature, humidity = read_dht22()
    current = read_acs712()

    sensor_data = {
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,
        "current": current
    }

    print(json.dumps(sensor_data, indent=4))

    time.sleep(2)
