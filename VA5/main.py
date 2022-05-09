import tkinter as tk
from random import randint

HEIGHT = 1000
WIDTH = 1000
window = tk.Tk()
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()
radii = 30
all_balls = []
class Ball:
    def __init__(self,balls):
        interx = WIDTH/2-radii
        intery = HEIGHT/2-radii
        x = randint(-interx,interx)
        y = randint(-intery,intery)
        self.xspeed=self.yspeed=5
        self.ball = canvas.create_oval(WIDTH/2-radii+x,HEIGHT/2-radii+y,WIDTH/2+radii+x,HEIGHT/2+radii+y)
        self.all_balls = balls
    def move(self):
        canvas.move(self.ball, self.xspeed, self.yspeed) 
    
    
 #   def update_speed(self):
        ballpos = canvas.coords(self.ball)
        if ballpos[0] < 0:
            self.xspeed = abs(self.xspeed)
        elif ballpos[2] > WIDTH:
            self.xspeed = -abs(self.xspeed)
        if ballpos[1] < 0:
            self.yspeed = abs(self.yspeed)
        elif ballpos[3] > HEIGHT:
            self.yspeed = -abs(self.yspeed)
        x1 = (ballpos[0] + ballpos[2])/2
        y1 = (ballpos[1] + ballpos[3])/2
        for i in self.all_balls:
            ballpos2 = canvas.coords(i.ball)
            x2 = (ballpos2[0] + ballpos2[2])/2
            y2 = (ballpos2[1] + ballpos2[3])/2
            dist = ((x1-x2)**2+(y1-y2)**2)**0.5

            if dist < 2*radii and dist != 0:
                scalar = ((i.xspeed-self.xspeed)*(x2-x1)+(i.yspeed-self.yspeed)*(y2-y1))/(dist**2)
                self.xspeed += scalar*(x2-x1)
                self.yspeed += scalar*(y2-y1)
                i.xspeed -= scalar*(x2-x1)
                i.yspeed -= scalar*(y2-y1)

def update_all(b):
  #  for i in b:
   #     i.update_speed()
    for i in b:
        i.move()

# ball = Ball(all_balls)

for i in range(10):
    all_balls.append(Ball(all_balls))
while True:
    canvas.after(30,update_all(all_balls))
    window.update()
window.mainloop()