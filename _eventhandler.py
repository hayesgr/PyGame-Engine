import pygame

def quit(self):
    self.run = 0
    return

def resize(self):
    if not self.full_screen:
        self.width, self.height = pygame.display.get_surface().get_size()
        self.window = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        self.scaled_background = pygame.transform.scale(self.AM.assets[self.bg],(self.width,self.height))
    return

def mouse_move(self):
    self.mh.move_update()
    return
def mouse_button_up(self):
    self.mh.set_state()
    return
def mouse_button_down(self):
    self.mh.set_state()
    return

#Only Keys that should effect every screen should be handled in here.
#All Other keys should make use of the keyboard_handler
def key_down(self):
    self.kbh.set_state(self.event_holder.key,1)
    return

def f1(self):
    self.full_screen = (not self.full_screen)
    if self.full_screen:
        self.swap_w = self.width
        self.swap_h = self.height
        self.width = 1920
        self.height = 1080
        self.window = pygame.display.set_mode((self.screen_w,self.screen_h),pygame.FULLSCREEN)
        self.scaled_background = pygame.transform.scale(self.AM.assets[self.bg],(self.screen_w,self.screen_h))
    else:
        self.width = self.swap_w
        self.height = self.swap_h
        self.window = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        self.scaled_background = pygame.transform.scale(self.AM.assets[self.bg],(self.width,self.height))
    return
key_switch = {pygame.K_F1:f1}

def key_up(self):
    rs = key_switch.get(self.event_holder.key)#event.key)
    if rs:
        rs(self)
    self.kbh.set_state(self.event_holder.key,0)
    return

switch = {pygame.QUIT:quit,pygame.VIDEORESIZE:resize,pygame.KEYDOWN:key_down,pygame.KEYUP:key_up,pygame.MOUSEMOTION:mouse_move,
    pygame.MOUSEBUTTONDOWN:mouse_button_down,pygame.MOUSEBUTTONUP:mouse_button_up}

def event_handler(self):
    for event in pygame.event.get():
        self.event_holder = event
        r = switch.get(event.type)
        if r:
            r(self)