from tkinter import *
import time


# define the Ball
class Ball:
    def __init__(self, canvas, color):    # need to draw on a canvas, and in a given colour
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # coordinates: top-l, bot-r
        self.canvas.move(self.id, 245, 100);   # move 245 px right, 100 down
        self.x = 3      # how many pixels will we move right initially?
        self.y = -3     # how many pixels will we move down initially?        
        self.canvas_height = self.canvas.winfo_height()     # get height of canvas        
        self.canvas_width = self.canvas.winfo_width()       # get width of canvas

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

ball = Ball(canvas, 'red')      # create a red ball


# use our own game loop
while True:
    ball.draw()
    app.update_idletasks()
    app.update()
    time.sleep(0.01)