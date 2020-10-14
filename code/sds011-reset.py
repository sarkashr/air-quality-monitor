from __init__ import SDS011
import time

# sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
# print(sensor.query())  # Gets (pm25, pm10)
# sensor.sleep()  # Turn off fan and diode
# print('set to sleep mode for 15 seconds')
# time.sleep(15)
# sensor.sleep(sleep=False)  # Turn on fan and diode
# print('set to active mode and waiting for 15 seconds')
# time.sleep(15)  # Allow time for the sensor to measure properly
# print(sensor.query())
# # There are other methods to configure the device, go check them out.
# print('end of reset script')
# sensor = None

print('initialising...')
sensor = SDS011("/dev/ttyUSB0", use_query_mode=False)
print('trying to set mode...')
sensor.set_report_mode(read=True, active=True)


# sensor.sleep()  # Turn off fan and diode
# print('set to sleep mode for 15 seconds')
# time.sleep(15)


print('trying to wake up... (in case in sleep mode)')
sensor.sleep(sleep=False)  # Turn on fan and diode in case it was in sleep mode
print('waiting for 15 seconds...')
time.sleep(15)  # Allow time for the sensor to measure properly
print('a test query -> ' + str(sensor.query()))
print('resetting mode...')
sensor.set_report_mode(read=True, active=True)
print('end of reset script')
sensor = None
