from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)

    # Correcting the image path
    img_path = "Interface Design.gif"  # Enter the path to your GIF image

    img = Image.open(img_path)
    lbl = Label(root)
    lbl.place(x=0, y=0)
    # mixer.music.load("music.mp3")  # Enter the path to your music file
    # mixer.music.play()

    # Looping through the frames of the GIF
    for frame in ImageSequence.Iterator(img):
        frame = frame.resize((1000, 500))
        img = ImageTk.PhotoImage(frame)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)

    root.destroy()


# Call the function to start playing the gif


# Start the main loop of Tkinter
