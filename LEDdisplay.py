# Python app to go control the display
from tkinter import *
root = Tk()
root.title('LED Display')
root.iconbitmap(r'C:\Users\nmark\Documents\GitHub\led-matrix-project\pyapp_icon.ico') 
root.geometry('400x400')

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root,text=hello)
    e.delete(0,'end')
    myLabel.pack(pady=10)

e = Entry(root, width=50, font=('Helvetica',30))
e.pack(padx=10,pady=10)

myButton = Button(root, text='Enter your name',command=myClick)
myButton.pack(pady=10)

root.mainloop()
