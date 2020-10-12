# import serial # package PySerial
# import struct
from sds011 import SDS011
import time
from datetime import datetime
import json
import paho.mqtt.publish as publish
import sys


def printValues(timing, values, unit_of_measure):
    if unit_of_measure == SDS011.UnitsOfMeasure.MassConcentrationEuropean:
        unit = 'µg/m³'
    else:
        unit = 'pcs/0.01cft'
    print("Waited %d secs\nValues measured in %s:    PM2.5  " %
          (timing, unit), values[1], ", PM10 ", values[0])


device_path = '/dev/ttyUSB0' # $ dmesg | grep tty
timeout = 9                         # timeout on serial line read
unit_of_measure = SDS011.UnitsOfMeasure.MassConcentrationEuropean
print('\n\n')
print('PRE __init__')
sensor = SDS011(device_path, timeout=timeout, unit_of_measure=unit_of_measure)
print('POST __init__')
print(sensor.workstate)
print(sensor.reportmode)
print("\n\n")
dictionary = {}

try:
    while True:
        sensor.workstate = SDS011.WorkStates.Measuring
        print('The sensor needs to warm up for 30 seconds!') # 60 seconds!')
        time.sleep(30)  # Should be 60 seconds to get qualified values. The sensor needs to warm up!
        # sensor.dutycycle = 5  # valid values between 0 and 30
        last = time.time()
        while True:
            last1 = time.time()
            values = sensor.get_values()
            ts = datetime.now()
            if values is not None:
                printValues(time.time() - last, values, sensor.unit_of_measure)
                dictionary = {
                    "time" : '{:%y-%m-%d %H:%M %S}'.format(ts), # with seconds
                    # "time" : '{:%y-%m-%d %H:%M}'.format(ts), # without seconds
                    "pm2.5" : values[1],
                    "pm10" : values[0],
                }
                break
            print("Waited %d seconds, no values read, wait 2 seconds, and try to read again" % (
                time.time() - last1))
            time.sleep(2)

        payload = json.dumps(dictionary, default=str)
        print(payload+"\n\n")
        publish.single(
            topic="aqm/kabul/station02", #"aqm/kabul/station01",
            payload=payload,
            hostname="broker.hivemq.com",
            port=8000,
            client_id="Station_02_Mikrorayan", #"Station_01_Office",
            transport="websockets",
        )

        print("Read was succesfull. Going to sleep now.")
        sensor.workstate = SDS011.WorkStates.Sleeping
        time.sleep(270)

except:
    sensor.reset()
    sensor = None
    sys.exit("\nSensor reset due to a KeyboardInterrupt or an error\n")
