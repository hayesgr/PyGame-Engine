import pygame
import random
import _balls


def load_content(self):
    #load content here initialy

    #Use dictionary for image management
    #self.images.append(pygame.image.load('assets/CircleR.png').convert_alpha())
    #self.images.append(pygame.image.load('assets/CircleG.png').convert_alpha())
    #self.images.append(pygame.image.load('assets/CircleB.png').convert_alpha())
    #self.images.append(pygame.image.load('assets/CircleY.png').convert_alpha())
    #self.images.append(pygame.image.load('assets/CircleP.png').convert_alpha())
    #self.background.append(pygame.image.load('assets/title.png').convert_alpha())
    #self.background.append(pygame.image.load('assets/black.png').convert_alpha())
    #self.scaled_background = pygame.transform.scale(self.background[self.bg],(self.width,self.height))
    self.AM.load_image("rCircle","CircleR.png")
    self.AM.load_image("gCircle","CircleG.png")
    self.AM.load_image("bCircle","CircleB.png")
    self.AM.load_image("yCircle","CircleY.png")
    self.AM.load_image("pCircle","CircleP.png")
    self.bg = self.AM.load_image("title","title.png")
    self.AM.load_image("black","black.png")
    self.scaled_background = pygame.transform.scale(self.AM.assets[self.bg],(self.width,self.height))
    
    random.seed(100)
    ball_count = 1000
    for i in range(0,ball_count):
        x = random.randint(50,300)
        y = random.randint(50,300)
        vx = random.randint(-400,400)
        vy = random.randint(-0,400)
        color = random.randint(0,4)
        b = _balls.Ball(x,y,vx,vy,color)
        self.balls.append(b)

    self.gt.set_timer()
    self.game_state = "intro"
    return