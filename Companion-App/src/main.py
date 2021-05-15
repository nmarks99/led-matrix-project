from os.path import supports_unicode_filenames
import serial
import time  
import utils

myport = utils.find_serial_port()   # Automatically find the serial port 

try:
    S = serial.Serial(myport,57600) # Open the serial port
except:
    print('Device not found')   # Notify user if device isn't found, then exit 
    time.sleep(2)
    exit()

print('==================')
print('LED MATRIX DISPLAY')
print('==================')

while True:
    msg = input('Enter a message: ')
    if msg == 'q':  # Quit the app if user enters 'q'
        break
    else:
        msg = msg + '\n'    # Add a newline to the message so the arduino knows it got it 
        S.write(msg.encode('utf-8'))    # Encode message to send over UART

time.sleep(0.5) # Wait half a second before closing serial port
S.close()

