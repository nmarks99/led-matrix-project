# Python app to go control the display

import tkinter 
import serial
import time

'''
S = serial.Serial('COM8',57600)
time.sleep(3)   # Wait for serial to open/arduino to reset
msg = "Hello\n"
S.write(msg.encode('utf-8'))
time.sleep(1)
S.close()
'''


root = tkinter.Tk()
root.title('LED Display')
root.iconbitmap(r'C:\Users\nmark\Documents\GitHub\led-matrix-project\pyapp_icon.ico') 
root.geometry('400x150')

def myClick():
    S = serial.Serial('COM8',57600)
    time.sleep(3)   # Wait for serial to open/arduino to reset
    msg = e.get()
    S.write(msg.encode('utf-8'))
    time.sleep(1)
    S.close()
    
    # msg = e.get()
    # myLabel = tkinter.Label(root,text=msg)
    # e.delete(0,'end')
    # myLabel.pack(pady=10)

e = tkinter.Entry(root, width=50, font=('Helvetica',30))
e.pack(padx=10,pady=10)

myButton = tkinter.Button(root, text='Enter',command=myClick)
myButton.pack(pady=10)

root.mainloop()