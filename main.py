import pygame
import serial
from ui_slider import Menu
from serial_sender import Serial_Sender
import threading




WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SD2023")
FPS = 120
clock = pygame.time.Clock()

tmp_list = [0] * 3600


pygame.init()
run = True

start_of_byte = True
tmp_outgoing_num = 0


my_slider = Menu(WIN)
my_sender = Serial_Sender("COM3", 12)
running_sender = True

should_send = True

def run_sender():
    while(running_sender):
        my_sender.run_sender(running_sender)

t1 = threading.Thread(target=run_sender)
t1.start()

while run:
    clock.tick(FPS)
    WIN.fill((255,255,255))
    my_slider.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()
pygame.quit()
running_sender=False
#ser.close()
