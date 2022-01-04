import pygame

class Mouse_Handler:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.old_x = 0
        self.old_y = 0
        self.num_buttons = 5
        self.b_state = []
        self.b_clicked = []
        for x in range(0,self.num_buttons):
            self.b_state.append(0)
            self.b_clicked.append(0)
        return

    def move_update(self):
        self.old_x,self.old_y = self.x,self.y
        self.x,self.y = pygame.mouse.get_pos()
        return

    def set_state(self):
        states = pygame.mouse.get_pressed(self.num_buttons)
        self.b_state[0],self.b_state[1],self.b_state[2],self.b_state[3],self.b_state[4] = states[0],states[1],states[2],states[3],states[4]
        self.b_clicked[0] = 1*(self.b_state[0]==1)
        self.b_clicked[1] = 1*(self.b_state[1]==1)
        self.b_clicked[2] = 1*(self.b_state[2]==1)
        self.b_clicked[3] = 1*(self.b_state[3]==1)
        self.b_clicked[4] = 1*(self.b_state[4]==1)
        return

    def is_pressed(self,Button):
        return self.b_state[Button]

    def was_clicked(self,Button):
        return self.b_clicked[Button]

    def reset_clicked(self,Button):
        self.b_clicked[Button]=0

    #Example Use
    #if self.mh.is_pressed(0):
    #    print("Button 0 pressed")
    #if self.mh.was_clicked(0):
    #    print("Button 0 was clicked")
    #    self.mh.reset_clicked(0)