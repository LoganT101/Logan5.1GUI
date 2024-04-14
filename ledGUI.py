from tkinter import *
import RPi.GPIO as GPIO

# window setup
root = Tk()
root.title("LED Control Board")

# gpio setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT) # blue
GPIO.setup(11, GPIO.OUT) # green
GPIO.setup(16, GPIO.OUT) # red

# toggle functions
def blueToggle():
    GPIO.output(8, True) # blue
    GPIO.output(11, False) # green
    GPIO.output(16, False) # red

def greenToggle():
    GPIO.output(8, False) # blue
    GPIO.output(11, True) # green
    GPIO.output(16, False) # red

def redToggle():
    GPIO.output(8, False) # blue
    GPIO.output(11, False) # green
    GPIO.output(16, True) # red

def off():
    GPIO.output(8, False) # blue
    GPIO.output(11, False) # green
    GPIO.output(16, False) # red

# select colour based on radio button input and call that toggle
def selectColour():
    selectedColour = colour.get()
    if selectedColour == "blue":
        blueToggle()
    elif selectedColour == "green":
        greenToggle()
    elif selectedColour == "red":
        redToggle()
    elif selectedColour == "off":
        off()

# exit program function
def exitProgram ():
    off()
    root.destroy()

# initalise colour variable that radio buttons use
colour = StringVar()

# radio buttons
Radiobutton(root, text="Blue", variable=colour, value="blue", command=selectColour).pack(anchor=W)
Radiobutton(root, text="Green", variable=colour, value="green", command=selectColour).pack(anchor=W)
Radiobutton(root, text="Red", variable=colour, value="red", command=selectColour).pack(anchor=W)
Radiobutton(root, text="Off", variable=colour, value="off", command=selectColour).pack(anchor=W)

# exit  button
exitButton = Button(root, text="Exit", command=exitProgram)
exitButton.pack()

# open window
root.mainloop()
