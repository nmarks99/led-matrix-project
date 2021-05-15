import serial.tools.list_ports  

def find_serial_port():
    try:
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if 'USB-SERIAL CH340' in p[1]:
                myport = p[0]
            else:
                return False
    except:
        print('No active ports')

    return myport