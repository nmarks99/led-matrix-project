import serial.tools.list_ports  

def find_serial_port():
    '''
    Returns a string corresponding to the serial port of the Arduino nano board.
    If the board is not found, return False
    '''
    myport = False 
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'USB-SERIAL CH340' in p[1]:
            myport = p[0]
    return myport

