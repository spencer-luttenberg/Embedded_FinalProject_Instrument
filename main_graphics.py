import pygame
from global_defines import *
import keyboard  # using module keyboard


def get_state():
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
    return tmp_outgoing_num


class Button():
    def __init__(self, window, x, y, img_path, img_grayed_path, img_pushed_path, scale):
        self.img = pygame.image.load(img_path).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height() 
        self.img = pygame.transform.scale(self.img, (int(width*scale), int(height*scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.window = window
        self.scale = scale

        self.img_pushed = img_pushed_path

        self.img_grayed = pygame.image.load(img_grayed_path).convert_alpha()
        self.img_grayed= pygame.transform.scale(self.img_grayed, (int(width*scale), int(height*scale)))
        self.img_pushed = pygame.image.load(img_pushed_path).convert_alpha()
        self.img_pushed= pygame.transform.scale(self.img_pushed, (int(width*scale), int(height*scale)))     
        
    def draw(self, input_state):
        #takes three input states: A: normal B: Grayed out C: Pressed
        pos = pygame.mouse.get_pos()
        pressed = False
        if(input_state==NORMAL_BUTTON_STATE):
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.window.blit(self.img_pushed, (self.rect.x, self.rect.y))
                    pressed = True
                else:
                    self.window.blit(self.img, (self.rect.x, self.rect.y))
            else:
                self.window.blit(self.img, (self.rect.x, self.rect.y))
        if(input_state==GRAYED_BUTTON_STATE):
            self.window.blit(self.img_grayed, (self.rect.x, self.rect.y))
        if(input_state==PUSHED_BUTTON_STATE):
            self.window.blit(self.img_pushed, (self.rect.x, self.rect.y))
        return pressed
    def set_image(self, input_img):
        self.img = pygame.image.load(input_img).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height() 
        self.img = pygame.transform.scale(self.img, (int(width*self.scale), int(height*self.scale)))

class main_fish:
    def __init__(self, window, x, y, scale):
        self.img_state_000 = pygame.image.load(STATE_000_IMG_PATH).convert_alpha()
        width = self.img_state_000.get_width()
        height = self.img_state_000.get_height() 
        self.img_state_000 = pygame.transform.scale(self.img_state_000, (int(width*scale), int(height*scale))) 
        self.rect = self.img_state_000.get_rect()
        self.rect.topleft = (x, y)
        self.window = window
        self.scale = scale
        self.img_state_001 = pygame.image.load(STATE_001_IMG_PATH).convert_alpha()
        self.img_state_001 = pygame.transform.scale(self.img_state_001, (int(width*scale), int(height*scale)))
        self.img_state_010 = pygame.image.load(STATE_010_IMG_PATH).convert_alpha()
        self.img_state_010 = pygame.transform.scale(self.img_state_010, (int(width*scale), int(height*scale)))
        self.img_state_011 = pygame.image.load(STATE_011_IMG_PATH).convert_alpha()
        self.img_state_011 = pygame.transform.scale(self.img_state_011, (int(width*scale), int(height*scale)))
        self.img_state_100 = pygame.image.load(STATE_100_IMG_PATH).convert_alpha()
        self.img_state_100 = pygame.transform.scale(self.img_state_100, (int(width*scale), int(height*scale)))
        self.img_state_101 = pygame.image.load(STATE_101_IMG_PATH).convert_alpha()
        self.img_state_101 = pygame.transform.scale(self.img_state_101, (int(width*scale), int(height*scale)))
        self.img_state_110 = pygame.image.load(STATE_110_IMG_PATH).convert_alpha()
        self.img_state_110 = pygame.transform.scale(self.img_state_110, (int(width*scale), int(height*scale)))
        self.img_state_111 = pygame.image.load(STATE_111_IMG_PATH).convert_alpha()
        self.img_state_111 = pygame.transform.scale(self.img_state_111, (int(width*scale), int(height*scale)))
    def draw(self, inputs):
        input_fish_state = inputs[3]
        if(input_fish_state==None):
            current_key_press = get_state()
        else:
            current_key_press= input_fish_state
        if(current_key_press==0):
            self.window.blit(self.img_state_000, (self.rect.x, self.rect.y))
        if(current_key_press==1):
            self.window.blit(self.img_state_001, (self.rect.x, self.rect.y))
        if(current_key_press==2):
            self.window.blit(self.img_state_010, (self.rect.x, self.rect.y))
        if(current_key_press==3):
            self.window.blit(self.img_state_011, (self.rect.x, self.rect.y))
        if(current_key_press==4):
            self.window.blit(self.img_state_100, (self.rect.x, self.rect.y))
        if(current_key_press==5):
            self.window.blit(self.img_state_101, (self.rect.x, self.rect.y))
        if(current_key_press==6):
            self.window.blit(self.img_state_110, (self.rect.x, self.rect.y))
        if(current_key_press==7):
            self.window.blit(self.img_state_111, (self.rect.x, self.rect.y))

class button_handler:
    def __init__(self, window):
        self.play_button = Button(window, 125, 325, 'resources/play_button_img.png', 'resources/play_button_img_grayed.png', 'resources/play_button_img_pushed.png', 1.0)
        self.pause_button = Button(window, 175, 325, 'resources/pause_button_img.png', 'resources/pause_button_img_grayed.png', 'resources/pause_button_img_pushed.png', 1.0)
        self.record_button = Button(window, 225, 325, 'resources/record_button_img.png', 'resources/record_button_img_grayed.png', 'resources/record_button_img_pushed.png', 1.0)
        self.import_song_button =  Button(window, 275, 325, 'resources/import_song_img.png', 'resources/import_song_pushed.png', 'resources/import_song_pushed.png', 1.0)
        self.import_track_button =  Button(window, 100, 375, 'resources/import_track_img.png', 'resources/import_track_img_pushed.png', 'resources/import_track_img_pushed.png', 1.0)
        self.export_track_button = Button(window, 200, 375, 'resources/export_track_img.png', 'resources/export_track_img_pushed.png', 'resources/export_track_img_pushed.png', 1.0)
        self.send_to_fish_button = Button(window, 300, 375, 'resources/send_to_fish_img.png', 'resources/send_to_fish_img_pushed.png', 'resources/send_to_fish_img_pushed.png', 1.0)
    def render_buttons(self, input_state):
        play_button_pushed = False
        record_button_pushed = False
        pause_button_pushed = False
        import_song_pushed = False
        import_track_pushed = False
        export_track_pushed = False
        send_to_fish_pushed = False
        if(input_state==PLAYING_SONG):
            play_button_pushed = self.play_button.draw(PUSHED_BUTTON_STATE)
            record_button_pushed = self.record_button.draw(GRAYED_BUTTON_STATE)
            pause_button_pushed = self.pause_button.draw(NORMAL_BUTTON_STATE)
            import_song_pushed = self.import_song_button.draw(NORMAL_BUTTON_STATE)
            import_track_pushed = self.import_track_button.draw(NORMAL_BUTTON_STATE)
            export_track_pushed = self.export_track_button.draw(NORMAL_BUTTON_STATE)
            send_to_fish_pushed = self.send_to_fish_button.draw(NORMAL_BUTTON_STATE)
        if(input_state==PAUSED):
            play_button_pushed = self.play_button.draw(NORMAL_BUTTON_STATE)
            record_button_pushed = self.record_button.draw(NORMAL_BUTTON_STATE)
            pause_button_pushed = self.pause_button.draw(NORMAL_BUTTON_STATE)
            import_song_pushed = self.import_song_button.draw(NORMAL_BUTTON_STATE)
            import_track_pushed = self.import_track_button.draw(NORMAL_BUTTON_STATE)
            export_track_pushed = self.export_track_button.draw(NORMAL_BUTTON_STATE)
            send_to_fish_pushed = self.send_to_fish_button.draw(NORMAL_BUTTON_STATE)
        if(input_state==RECORDING_SONG):
            play_button_pushed = self.play_button.draw(GRAYED_BUTTON_STATE)
            record_button_pushed = self.record_button.draw(PUSHED_BUTTON_STATE)
            pause_button_pushed = self.pause_button.draw(NORMAL_BUTTON_STATE)
            import_song_pushed = self.import_song_button.draw(NORMAL_BUTTON_STATE)
            import_track_pushed = self.import_track_button.draw(NORMAL_BUTTON_STATE)
            export_track_pushed = self.export_track_button.draw(NORMAL_BUTTON_STATE)
            send_to_fish_pushed = self.send_to_fish_button.draw(NORMAL_BUTTON_STATE)
        return play_button_pushed, record_button_pushed, pause_button_pushed, import_song_pushed, import_track_pushed, export_track_pushed, send_to_fish_pushed

class Input_UI:
    def __init__(self, window, bg="gray") -> None:
        self.window = window
        self.bg = bg
        self.tmp_val = 0.0
        self.slider = Slider((window.get_size()[0]//2, window.get_size()[1]//2+200), (400,30), 0, 0, 100)
        self.main_button_handler = button_handler(window)


    def run(self, INPUTS):
        #input: position pointer, output state, percentage of song, output_fish_state (NONE IF NOT PLAYING)]
        #output: [play_button_pressed, record_button_pressed, pause_button_pressed, slider_new_percentage]

        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        pos_of_ptr = INPUTS[0]
        input_state = INPUTS[1]
        percentage = INPUTS[2]
        output_of_fish = INPUTS[3]
        #sliders
        if(input_state==PAUSED):
            if self.slider.container_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    self.slider.grabbed = True
            if not mouse[0]:
                self.slider.grabbed = False
            if self.slider.button_rect.collidepoint(mouse_pos):  
                self.slider.hover()
            if self.slider.grabbed:
                self.slider.move_slider(mouse_pos)
                self.slider.hover()
            else:
                self.slider.hovered = False
        else:
            self.slider.hovered = False
            self.slider.set_value(percentage)
        self.slider.render(self.window)
        play_pushed, record_pushed, pause_pushed, import_song_pushed, import_track_pushed, export_track_pushed, send_to_fish_pushed  = self.main_button_handler.render_buttons(input_state)
        return [play_pushed, record_pushed, pause_pushed, self.slider.get_value(), import_song_pushed, import_track_pushed, export_track_pushed, send_to_fish_pushed]

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max

        

        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage
        #pygame.draw.circle(WINDOW, GREEN, (160, 70), 30)
        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

        # label
        
    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
    def hover(self):
        self.hovered = True
    def render(self, app):
        pygame.draw.rect(app, "darkgray", self.container_rect)
        #pygame.draw.circle(app, (77,77,77), [self.slider_left_pos, self.slider_top_pos+self.size[1]/2], self.size[1]/2)
        tmp_rect = pygame.Rect(self.container_rect.left, self.container_rect.top, self.button_rect.center[0]-self.container_rect.left, self.container_rect.height)
        pygame.draw.rect(app, (77,77,77), tmp_rect)
        tmp_radius = self.size[1]/2
        if(self.hovered):
            tmp_radius=tmp_radius*1.2
        pygame.draw.rect(app, "black", self.button_rect)
        #pygame.draw.circle(app, "black", self.button_rect.center, tmp_radius)
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos
        return (button_val/val_range)*(self.max-self.min)+self.min
    def set_value(self, val):
        val_out = (self.slider_right_pos - self.slider_left_pos)*(val/(self.max-self.min))
        self.button_rect.centerx = self.slider_left_pos + val_out

