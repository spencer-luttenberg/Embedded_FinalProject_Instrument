import pygame



class Menu:
    def __init__(self, window, bg="gray") -> None:
        self.window = window
        self.bg = bg
        self.tmp_val = 0.0
        self.sliders = [
            Slider((window.get_size()[0]//2, window.get_size()[1]//2+200), (400,30), 0, 0, 100)
        ]

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for slider in self.sliders:
            if slider.container_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    slider.grabbed = True
            if not mouse[0]:
                slider.grabbed = False
            if slider.button_rect.collidepoint(mouse_pos):  
                slider.hover()
            if slider.grabbed:
                slider.move_slider(mouse_pos)
                slider.hover()
            else:
                slider.hovered = False
            slider.render(self.window)

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
        pygame.draw.circle(app, (77,77,77), [self.slider_left_pos, self.slider_top_pos+self.size[1]/2], self.size[1]/2)
        pygame.draw.circle(app, "darkgray", [self.slider_left_pos+self.container_rect.width, self.slider_top_pos+self.size[1]/2], self.size[1]/2)
        tmp_rect = pygame.Rect(self.container_rect.left, self.container_rect.top, self.button_rect.center[0]-self.container_rect.left, self.container_rect.height)
        pygame.draw.rect(app, (77,77,77), tmp_rect)
        tmp_radius = self.size[1]/2
        if(self.hovered):
            tmp_radius=tmp_radius*1.2
        pygame.draw.circle(app, "black", self.button_rect.center, tmp_radius)
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos
        return (button_val/val_range)*(self.max-self.min)+self.min
    def set_value(self, val):
        val_out = (self.slider_right_pos - self.slider_left_pos)*(val/(self.max-self.min))
        self.button_rect.centerx = self.slider_left_pos + val_out

