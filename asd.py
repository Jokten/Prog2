from tkinter import *
class Ball:
    def __init__ (self,canvas,x,y,diameter,xVelo,yVelo,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelo = xVelo
        self.yVelo = yVelo
    def move(self):
        coordinates = self.canvas.coords(self.image)
        if (coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0):
            self.xVelo = -self.xVelo
        if (coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0):
            self.yVelo = -self.yVelo
        self.canvas.move(self.image,self.xVelo,self.yVelo)
import time
HEIGHT = 500
WIDTH = 500
window = Tk()


canvas = Canvas(window,height=HEIGHT,width = WIDTH)
canvas.pack()
basket_ball = Ball(canvas,0,0,100,1,1,"orange")
soccer_ball = Ball(canvas,399,399,499,1,1,"black")

while True:
    basket_ball_coords = canvas.coords(basket_ball.image)
    soccer_ball_coords = canvas.coords(soccer_ball.image)
    basket_ball.move()
    soccer_ball.move()
    print (basket_ball_coords)
    print (soccer_ball_coords)
    if basket_ball_coords[2] == soccer_ball_coords[0] and ((soccer_ball_coords[3] - basket_ball_coords[3])<= 100 and (soccer_ball_coords[3] - basket_ball_coords[3])> -101):
        basket_ball.xVelo = -basket_ball.xVelo
        soccer_ball.xVelo = -soccer_ball.xVelo
    if basket_ball_coords[3] == soccer_ball_coords[1] and ((soccer_ball_coords[2]- basket_ball_coords[2]<=100)and (soccer_ball_coords[2] - basket_ball_coords[2])> -101):
        basket_ball.yVelo = -basket_ball.yVelo
        soccer_ball.yVelo = -soccer_ball.yVelo
    if basket_ball_coords[0] == soccer_ball_coords[2] and ((soccer_ball_coords[3] - basket_ball_coords[3]) <= 100 and (soccer_ball_coords[3] - basket_ball_coords[3]) > -101):
        basket_ball.xVelo = -basket_ball.xVelo
        soccer_ball.xVelo = -soccer_ball.xVelo
    if basket_ball_coords[1] == soccer_ball_coords[3] and ((soccer_ball_coords[2]- basket_ball_coords[2]<=100)and (soccer_ball_coords[2] - basket_ball_coords[2])> -101):
        basket_ball.yVelo = -basket_ball.yVelo
        soccer_ball.yVelo = -soccer_ball.yVelo
    window.update()
    time.sleep(0.01)


window.mainloop()