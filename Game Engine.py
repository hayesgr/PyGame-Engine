import pygame
from _eventhandler import event_handler
from _load_content import load_content
from _update import update
from _renderer import renderer
from _timer import Timer
from keyboard_handler import Keyboard_Handler
from mouse_handler import Mouse_Handler
from asset_manager import Asset_Manager
from _profile import profile
PROFILE = False          #Set to true to profile game, false to not profile game

class Game:

    def __init__(self,width,height):
        self.title = "Game Title"
        self.game_state = "intro"
        self.full_screen = 0
        self.screen_w = 1920    #Monitor width
        self.screen_h = 1080    #Monitor height
        self.event_holder = None   #holds events to share across engine
        self.run = 1   
        self.swap_w = 0         #for swapping from FS to window
        self.swap_h = 0         #for swapping from FS to window
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height),pygame.RESIZABLE)
        pygame.display.set_caption(self.title)
        pygame.font.init()
        pygame.mixer.init()
        self.gt = Timer()       #game timer
        self.kbh = Keyboard_Handler()
        self.mh = Mouse_Handler()
        self.AM = Asset_Manager()
        
        
        #game content
        #self.images = []                #list of images
        self.balls = []                 #list of balls
        #self.background = []            #list of backgrounds
        self.bg = 0                     #determines what background is in use
        self.scaled_background = None   #used to increase performance only need to scale 1 time.
        


    def main_loop(self):
        load_content(self)
        while self.run:
            event_handler(self)
            update(self)
            renderer(self)
        return

def main():
    g = Game(960,540)
    g.main_loop()
    pygame.quit
    return

if not PROFILE:
    if __name__ == "__main__":
        main()
else:
    profile()