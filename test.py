
import serial
import time

S = serial.Serial('COM8',57600)
time.sleep(3)   # Wait for serial to open/arduino to reset
msg = "hey!!\n"
S.write(msg.encode('utf-8'))
time.sleep(1)
S.close()