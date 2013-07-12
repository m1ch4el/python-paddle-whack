from tkinter import *
import time

app = Tk()

app.title("Paddle Whack")
app.resizable(0, 0)                 # make window a fixed size
app.wm_attributes("-topmost", 1)    # bring window to front

# create a canvas 500 by 400 pixels, with no border
canvas = Canvas(app, width=500, height=400,
                bd=0, highlightthickness=0)

canvas.pack()       # tell canvas to size itself
app.update()        # without this the canvas height and width is not set correctly

# use our own game loop
while True:
    app.update_idletasks()
    app.update()
    time.sleep(0.01)