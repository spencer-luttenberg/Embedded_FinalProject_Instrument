import pygame
import serial
from main_graphics import Input_UI
from serial_sender import Serial_Sender
import threading
from global_defines import *
from main_controller import main_controller
from main_graphics import main_fish

  
# Function for opening the 
# file explorer window



WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SD2023")
FPS = 120
clock = pygame.time.Clock()


pygame.init()
run = True

start_of_byte = True
tmp_outgoing_num = 0
main_fish_control =  main_fish(WIN, 10, 50, 0.23)

main_UI = Input_UI(WIN)
main_controller = main_controller()
my_sender = Serial_Sender("COM3", 12)
running_sender = True
should_send = True




def run_sender_thread():
    while(running_sender):
        my_sender.run_sender(running_sender)
t1 = threading.Thread(target=run_sender_thread)
t1.start()

global prev_outputs
prev_outputs = [0, PAUSED, 0, None]
while run:
    clock.tick(FPS)
    WIN.fill((255,255,255))

    main_outputs = main_UI.run(prev_outputs) #takes an input of current state taken from the array; outputs current "State" of UI
    prev_outputs = main_controller.handle_control(main_outputs)
    main_fish_control.draw(prev_outputs)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()
pygame.quit()
running_sender=False
#ser.close()
