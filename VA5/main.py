import tkinter as tk
from random import randint
from random import choice

<<<<<<< HEAD
global speed
=======
HEIGHT = 500
WIDTH = 500
window = tk.Tk()
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()
radii = 30
all_balls = []
>>>>>>> 6938449fa0b5d4fc3f8ac31cc94961ec15d037cb
class Ball:
    def __init__(self,balls):
        interx = WIDTH/2-radii
        intery = HEIGHT/2-radii
        run = 1
        while run==1:
            x = randint(-interx,interx)
            y = randint(-intery,intery)
            x1 = WIDTH/2+x
            y1 = HEIGHT/2+y
            run = 0
            for i in balls:
                ballpos2 = canvas.coords(i.ball)
                x2 = (ballpos2[0] + ballpos2[2])/2
                y2 = (ballpos2[1] + ballpos2[3])/2
                dist = ((x1-x2)**2+(y1-y2)**2)**0.5
                if dist < 2*radii:
                    run = 1
                    break
        self.xspeed=self.yspeed=1
        self.ball = canvas.create_oval(WIDTH/2-radii+x,HEIGHT/2-radii+y,WIDTH/2+radii+x,HEIGHT/2+radii+y, fill=choice(colors))
        self.all_balls = balls
    def move(self):
        canvas.move(self.ball, self.xspeed, self.yspeed) 
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

class Hole:
    def __init__(self,x,y,balls) -> None:
        
        self.hole = canvas.create_oval(x-radii_hole,-radii_hole+y,radii_hole+x,radii_hole+y, fill='black')
        self.all_ball = balls
        self.x = x
        self.y = y
    def remove_balls(self):
        for i in self.all_ball:
            ballpos2 = canvas.coords(i.ball)
            x2 = (ballpos2[0] + ballpos2[2])/2
            y2 = (ballpos2[1] + ballpos2[3])/2
            dist = ((self.x-x2)**2+(self.y-y2)**2)**0.5

            if dist < radii+radii_hole and dist != 0:
                canvas.delete(i.ball)
                self.all_ball.remove(i)
                print('deleted')

def create_balls(event):
    n = int(entry.get())
    global speed
    speed = int(entry2.get())
    print('heh')
    for i in range(n):
        all_balls.append(Ball(all_balls))

def remove_all(event):
    #canvas.delete('all')
    for i in all_balls:
        canvas.delete(i.ball)
        all_balls.remove(i)

def update_all(b,h):
    for i in b:
        i.move()
    for i in h:
        i.remove_balls()

speed = 6
HEIGHT = 1000
WIDTH = 1000
window = tk.Tk()
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH, bg='green')
canvas.pack(side='left')
frame = tk.Frame(window, bg='brown')
frame.pack(side='right')
radii = 30
all_balls = []
radii_hole = 60
colors = ['red', 'blue', 'white', 'yellow']
label = tk.Label(frame,text='Number of balls')
entry = tk.Entry(frame)
label.pack()
entry.pack()
label2 = tk.Label(frame,text='Speed')
entry2 = tk.Entry(frame)
label2.pack()
entry2.pack()
start_button = tk.Button(frame, text="Start",
    width=25,
    height=5,
    bg="green"
)
stop_button = tk.Button(frame, text="Stop",
    width=25,
    height=5,
    bg="red"
)
start_button.bind("<Button-1>", create_balls)
stop_button.bind("<Button-1>", remove_all)
start_button.pack()
stop_button.pack()


h = []
h.append(Hole(0,0,all_balls))
h.append(Hole(0,HEIGHT,all_balls))
h.append(Hole(WIDTH,HEIGHT,all_balls))
h.append(Hole(WIDTH,0,all_balls))
while True:
    canvas.after(speed,update_all(all_balls, h))
    window.update()
    window.update_idletasks()
window.mainloop()