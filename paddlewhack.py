from tkinter import *
import time
import random


# define the Ball
class Ball:
    def __init__(self, canvas, paddle, color):    # need to draw on a canvas, and in a given colour
        self.canvas = canvas
        self.paddle = paddle        # also need to know where the paddle is
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # coordinates: top-l, bot-r
        self.canvas.move(self.id, 245, 100);   # move 245 px right, 100 down
        self.x = random.randint(-3, 3)      # how many pixels will we move right initially?
        self.y = random.randint(-3, 3)      # how many pixels will we move down initially?        
        self.canvas_height = self.canvas.winfo_height()     # get height of canvas        
        self.canvas_width = self.canvas.winfo_width()       # get width of canvas
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)       # move x pixel right, y pixel down
        pos = self.canvas.coords(self.id)               # get current x and y coordinates of ourself (the ball)

        if pos[1] <= 0:                     # if top of the ball hits top of screen
            self.y = reverse(self.y)        # ... reverse up/down direction
        if pos[3] >= self.canvas_height:    # if bottom of ball hits bottom of screen
            self.y = reverse(self.y)        # ... reverse up/down direction

        if pos[0] <= 0:                     # if left side of the ball hits left screen border
            self.x = reverse(self.x)        # ... reverse left/right direction
        if pos[2] >= self.canvas_width:     # if right side of ball hits right screen border
            self.x = reverse(self.x)        # ... reverse left/right direction

        if self.hit_paddle():
            self.y = reverse(self.y)
            
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            
    def hit_paddle(self):
        paddle_pos = self.canvas.coords(self.paddle.id)
        ball_pos = self.canvas.coords(self.id)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                return True
        return False


# define the Paddle
class Paddle:
    def __init__(self, canvas, color):      # like ball, need to draw on a canvas, and in a given colour
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0;
            
    def turn_left(self, event):
        self.x = -2
        
    def turn_right(self, event): 
        self.x = 2
        
# a helper function to reverse a direction
def reverse(direction):
    return direction * -1


# this is where the game script begins
app = Tk()

app.title("Paddle Whack")
app.resizable(0, 0)                 # make window a fixed size
app.wm_attributes("-topmost", 1)    # bring window to front

# create a canvas 500 by 400 pixels, with no border
canvas = Canvas(app, width=500, height=400,
                bd=0, highlightthickness=0)

canvas.pack()       # tell canvas to size itself
app.update()        # without this the canvas height and width is not set correctly

paddle = Paddle(canvas, 'blue') # create a blue paddle
ball = Ball(canvas, paddle, 'red')      # create a red ball


# use our own game loop
while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    app.update_idletasks()
    app.update()
    time.sleep(0.01)