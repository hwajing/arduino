import serial
import time

# https://www.instructables.com/id/Arduino-Python-Communication-via-USB/

arduino = serial.Serial('COM5', 9600, timeout=.1)
# arduino = serial.Serial('COM5', 115200, timeout=.1) Why 115200?

time.sleep(1) # give the connection a second to settle

# Python => Arduino
arduino.write("Hello from Python!")
while True:
    data = arduino.readline()
    if data:
        print(data.rstrip('\n')) # strip out the new lines for now

