import pygame

#renderer

def intro_r(self):
    self.window.blit(self.scaled_background,(0,0))
    return

def menu_r(self):
    self.window.fill((0,0,255))
    return

def options_r(self):
    return

def play_r(self):
    #self.window.fill((0,0,0))
    self.window.blit(self.scaled_background,(0,0))
    for b in self.balls:
        #self.window.blit(self.images[b.color],(b.x-32,b.y-32))
        self.window.blit(self.AM.assets[b.color],(b.x-32,b.y-32))
    return

def credits_r(self):
    return

def end_r(self):
    return
switch_r = {"intro":intro_r,"menu":menu_r,"options":options_r,"play":play_r,"credits":credits_r,"end":end_r}
def renderer(self):
    #Where nested code used to be
    r = switch_r.get(self.game_state)
    if r:
        r(self)
    pygame.display.update()
    return

