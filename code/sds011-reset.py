from __init__ import SDS011
import time

sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
print(sensor.query())  # Gets (pm25, pm10)
sensor.sleep()  # Turn off fan and diode
print('set to sleep mode for 15 seconds')
time.sleep(15)
sensor.sleep(sleep=False)  # Turn on fan and diode
print('set to active mode  15 seconds')
time.sleep(15)  # Allow time for the sensor to measure properly
print(sensor.query())
# There are other methods to configure the device, go check them out.
print('end of reset script')
# sensor = None
