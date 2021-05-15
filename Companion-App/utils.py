import serial.tools.list_ports  

def find_serial_port():
    myport = False 
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'USB-SERIAL CH340' in p[1]:
            myport = p[0]
    return myport

