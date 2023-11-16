from global_defines import *



class main_controller:
    def __init__(self):
        self.current_song_array = [0] * FILE_LENGTH
        self.current_state = PAUSED
    def handle_control(self, inputs):
        if(self.current_state==PAUSED):
            print("Paused!")
        if(self.current_state==PLAYING_SONG):
            print("Playing song!")
        if(self.current_state==RECORDING_SONG):
            print("Recording song!")

            
        