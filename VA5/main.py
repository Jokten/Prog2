import tkinter as tk

HEIGHT = 500
WIDTH = 500
window = tk.Tk()
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

class Ball:
    def __init__(self):
        self.xspeed=self.yspeed=3
        self.ball = canvas.create_oval(150,250,200,300)
        
    def move(self):
        canvas.move(self.ball, self.xspeed, self.yspeed)
        ballpos = canvas.coords(self.ball)
        if ballpos[0] < 0 or ballpos[2] > WIDTH:
            self.xspeed = -self.xspeed
        if ballpos[1] < 0 or ballpos[3] > HEIGHT:
            self.yspeed = -self.yspeed
ball = Ball()
while True:

    canvas.after(30,ball.move())
    window.update()
window.mainloop()