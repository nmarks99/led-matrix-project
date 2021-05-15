from os.path import supports_unicode_filenames
import serial
import time  
import utils

myport = utils.find_serial_port()

try:
    S = serial.Serial(myport,57600) # Open the serial port
except:
    print('Device not found')
    time.sleep(2)
    exit()

print('==================')
print('LED MATRIX DISPLAY')
print('==================')

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    else:
        msg = msg + '\n'
        S.write(msg.encode('utf-8'))

time.sleep(0.5)
S.close()

