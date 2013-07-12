from tkinter import *
import time


# define the Ball
class Ball:
    def __init__(self, canvas, color):    # need to draw on a canvas, and in a given colour
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # coordinates: top-l, bot-r
        self.canvas.move(self.id, 245, 100);   # move 245 px right, 100 down
        
    def draw(self):
        pass    # we will add code here shortly
        


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
    app.update_idletasks()
    app.update()
    time.sleep(0.01)