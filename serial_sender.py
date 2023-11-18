import serial
import time
import keyboard  # using module keyboard



class Serial_Sender:
    def __init__(self, COM_PORT, FREQ):
        #self.ser = serial.Serial('COM3', 9600, timeout=1000, parity=serial.PARITY_EVEN, stopbits=1)
        self.FREQ = FREQ
    def run_sender(self, should_send):
        if(should_send):
            tmp_outgoing_num=0
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):
                    tmp_outgoing_num+=4
                if keyboard.is_pressed('w'):
                    tmp_outgoing_num+=2
                if keyboard.is_pressed('e'):
                    tmp_outgoing_num+=1             
            except:
                pass
            outgoing_data = tmp_outgoing_num.to_bytes(1, 'big')
            #self.ser.write(outgoing_data)
            #print(outgoing_data)
        time.sleep(1/self.FREQ)