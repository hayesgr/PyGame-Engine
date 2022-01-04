class Ball:
        
    def __init__(self,x,y,vx,vy,c):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.color=c
        return

    
    def update(self,w,h,t):
        time = float(t)/float(1000000)
        #print(time)
        xp = float(self.vx)*float(time)
        yp= float(self.vy)*float(time)
        self.x += xp
        self.y += yp
        #print (str(xp) +"," +str(yp))
        if self.x<32:
            self.vx = 0 - self.vx
            self.x += (32-self.x)
        if self.y<32:
            self.vy = 0 - self.vy
            self.y += (32-self.y)
        if self.x+32>w:
            self.vx = 0 - self.vx
            self.x -= (self.x+32)-w
        if self.y+32>h:
            self.vy = 0 - self.vy
            self.y -= (self.y+32)-h
        return