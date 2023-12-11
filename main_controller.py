from global_defines import *
import threading
import time
import keyboard
import vlc
from tkinter import filedialog
import csv
import serial
from tk_prompt import tkInterSerialSender
class main_controller:
    def __init__(self):
        self.current_song_array = [0] * FILE_LENGTH
        self.current_poisition_pointer = 0
        self.current_state = PAUSED
        self.currently_playing = False
        self.current_fish_output = 0
        self.currently_recording=False
        self.input_song_path = DEFAULT_SONG
        self.current_song = vlc.MediaPlayer(self.input_song_path)
        self.current_song_media = vlc.Media(self.input_song_path)
        #self.music_player = vlc.Instance()
        #self.media_list = self.music_player.media_list_new()
        #self.media_player = self.music_player.media_list_player_new()
        #self.media = self.music_player.media_new(self.input_song_path)
        #self.media_list.add_media(self.media)
        #self.media_player.set_media_list(self.media_list)
        #self.music_player.vlm_set_loop(self.input_song_path, True)
        
        
    def import_file(self, file_type):
        if(file_type==SONG_TYPE):
            filename = filedialog.askopenfilename(initialdir = "",
                                            title = "Select a File",
                                            filetypes = (("MP3s",
                                                            "*.mp3*"),
                                                        ("all files",
                                                            "*.*")))
        if(file_type==CSV_TYPE):
            filename = filedialog.askopenfilename(initialdir = "",
                                            title = "Select a File",
                                            filetypes = (("CSVs",
                                                            "*.csv*"),
                                                        ("all files",
                                                            "*.*")))       
        # Change label contents
        return filename
    def save_file(self):
        filename_stuff = [('CSV File', '*.csv')]
        file = filedialog.asksaveasfile(filetypes = filename_stuff, defaultextension = filename_stuff)
        if(file!=None): 
            tmp_string_file = ','.join(map(str, self.current_song_array))
            file.write(tmp_string_file)
            file.close()
        # # open the file in the write mode
        # tmp_file = open(file, 'w+')
        # # create the csv writer
        # writer = csv.writer(tmp_file)
        # writer.writerow(self.current_song_array) 
        # tmp_file.close()
    def playing_thread_loop(self):
        while(self.currently_playing==True):
            self.current_fish_output=self.current_song_array[self.current_poisition_pointer]
            if(self.current_poisition_pointer<len(self.current_song_array)):
                self.current_poisition_pointer+=1
            time.sleep(1/GLOBAL_SONG_FREQ)
    def start_playing(self):
        self.playing_thread = threading.Thread(target=self.playing_thread_loop)
        self.playing_thread.start()


    def recording_thread_loop(self):
        while(self.currently_recording==True):
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
            self.current_song_array[self.current_poisition_pointer]=tmp_outgoing_num
            if(self.current_poisition_pointer<len(self.current_song_array)):
                self.current_poisition_pointer+=1
            time.sleep(1/GLOBAL_SONG_FREQ)
    def start_recording(self):
        self.recording_thread = threading.Thread(target=self.recording_thread_loop)
        self.recording_thread.start()

    def handle_control(self, inputs):
        """_summary_

        Args:
            inputs ([play_button_pressed, record_button_pressed, pause_button_pressed, slider_new_percentage]): _description_
            outputs(position pointer, output state, percentage of song, output_fish_state (NONE IF NOT PLAYING)])
        """

        play_button_pressed = inputs[0]
        record_button_pressed = inputs[1]
        pause_button_pressed = inputs[2]
        slider_new_percentage = (inputs[3])/100 # convert to decimal

        import_song_pushed = inputs[4] 
        import_track_pushed = inputs[5]
        export_track_pushed = inputs[6]
        send_to_fish_pushed = inputs[7]
        input_slider_pointer = int(len(self.current_song_array)*slider_new_percentage)
        
        if(import_song_pushed==True):
            path = self.import_file(SONG_TYPE)
            if(path!=None):
                self.current_song.pause()
                self.current_song_media = vlc.Media(path)
                self.current_song.set_media(self.current_song_media)
        if(export_track_pushed==True):
            self.save_file()
        if(import_track_pushed==True):
            tmp_file_path = self.import_file(CSV_TYPE)
            if(tmp_file_path!=""):
                with open(tmp_file_path) as file_obj: 
                    reader_obj = csv.reader(file_obj) 
                    for row in reader_obj: 
                        tmp_list = row
                        tmp_int_list = [int(i) for i in tmp_list]
                        self.current_song_array = tmp_int_list
        if(send_to_fish_pushed==True):
            #self.ser = serial.Serial('COM3', 9600, timeout=1000, parity=serial.PARITY_EVEN, stopbits=1)
            #tmp_outgoing_bytes = [i.to_bytes(1, 'big') for i in self.current_song_array]
            #tmp_list = self.current_song_array

            tmp_tk_object = tkInterSerialSender(self.current_song_array)
            #tmp_list.inster(0, X)
            #tmp_byte_array = bytearray(tmp_list)
            #self.ser.write(tmp_byte_array)
            #self.ser.close()
            
        #inputs: play, record, pause; slider
        #outputs: position pointer, output state, percentage of song, output_fish_state (NONE IF NOT PLAYING)
        if(self.current_state==PAUSED):
            if(play_button_pressed==True):
                self.current_state = PLAYING_SONG
                self.currently_playing=True
                self.start_playing()
                self.current_song.play()
            if(record_button_pressed==True):
                self.current_state = RECORDING_SONG
                self.currently_recording=True
                self.start_recording()
                self.current_song.play()
            if(pause_button_pressed==True):
                pass
            else:
                self.current_poisition_pointer=input_slider_pointer
            #GLOBAL_SONG_FREQ; 1/GLOBAL_SONG_FREQ*PTR*1000 = MS
            if((1/GLOBAL_SONG_FREQ)*self.current_poisition_pointer*1000!=0):
                #self.media.add_option('start-time=60.00')
                if(int((1/GLOBAL_SONG_FREQ)*self.current_poisition_pointer*1000)<self.current_song.get_length()):
                    if(self.current_song.get_state()==6):
                        self.current_song.set_media(self.current_song_media)
                    self.current_song.set_time(int((1/GLOBAL_SONG_FREQ)*self.current_poisition_pointer*1000))

                #self.current_song.
            #self.current_song.set_time(1)
            return[input_slider_pointer, self.current_state, slider_new_percentage, None]
        elif(self.current_state==PLAYING_SONG):
            if(play_button_pressed==True):
                pass
            if(record_button_pressed==True):
                pass
            if(pause_button_pressed==True):
                #join playing thread-> set state to paused
                self.currently_playing=False
                self.playing_thread.join()
                self.current_state=PAUSED
                self.current_song.pause()
            return[self.current_poisition_pointer, self.current_state, (self.current_poisition_pointer/len(self.current_song_array))*100, self.current_fish_output]
        elif(self.current_state==RECORDING_SONG):
            #join playing thread-> set state to paused
            #self.playing_thread.join()
            #self.current_state=PAUSED
            if(play_button_pressed==True):
                pass
            if(record_button_pressed==True):
                pass
            if(pause_button_pressed==True):
                #join playing thread-> set state to paused
                self.currently_recording=False
                self.recording_thread.join()
                self.current_state=PAUSED
                self.current_song.pause()
            return[self.current_poisition_pointer, self.current_state, (self.current_poisition_pointer/len(self.current_song_array))*100, None]



            
        