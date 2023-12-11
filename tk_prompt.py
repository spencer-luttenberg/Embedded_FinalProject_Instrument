from tkinter import *
import serial
import time
OPTIONS = [
'0', 
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8'            
] #etc

class tkInterSerialSender:
    def __init__(self, song_array):
        self.master = Tk()
        self.var = StringVar()
        self.label = Label(self.master, textvariable=self.var, relief=RAISED )
        self.var.set("Enter a song ID position")
        self.label.pack()
        self.variable = StringVar(self.master)
        self.variable.set(OPTIONS[0]) # default value
        self.w = OptionMenu(self.master, self.variable, *OPTIONS)
        self.w.pack()   
        self.button = Button(self.master, text="Send to Fish", command=self.sendToFish)
        self.button.pack()
        self.song_array=song_array
        self.ser = serial.Serial('COM3', 3600, timeout=1000, parity=serial.PARITY_EVEN, stopbits=1)
        mainloop()
    def sendToFish(self):
        tmp_return_val = self.variable.get()
        tmp_list = self.song_array
        tmp_list.insert(0, int(tmp_return_val))
        i = 0
        while(i < 3600):
            i+=1
            tmp_byte = tmp_list[i]
            time.sleep(0.001)
            self.ser.write(bytes(tmp_byte))

        #tmp_byte_array = bytearray(tmp_list)
        #print(self.ser.write(tmp_byte_array))
        #print(tmp_byte_array)
        #self.master.destroy()
        print("Sent Message to Fish!")
        #self.ser.close()
        



