import os
from os import listdir
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

import random

class Tile():
    def __init__(self, image, edges):
        self.image = image
        self.edges = edges

    



folder_dir = "C:\\Users\\Rockwell\\OneDrive\Documents\\Python\\Collapse"
tileList = []
imgList = []
frameList = []
#for images in os.listdir(folder_dir):
#    if(images.endswith(".png")):
#        imageList.append(folder_dir + "\\" + images)

#for dir in imageList:
#    print(dir)

tile0 = Tile("tile0.png", "a,a,a,a")
tile1 = Tile("tile1.png", "b,b,b,a")
tile2 = Tile("tile2.png", "b,b,b,b")
tile3 = Tile("tile3.png", "c,c,c,b")
tile4 = Tile("tile4.png", "c,c,c,c")

tileList.append(tile0)
tileList.append(tile1)
tileList.append(tile2)
tileList.append(tile3)
tileList.append(tile4)

root = Tk()
# Styling -------------------------------
s = ttk.Style()
s.configure("mainframe.TFrame", background = "#2A2F4F") #purple
s.configure("tile.TFrame", background="#05BFDB")    #teal
s.configure("tile1.TFrame", background="#F3E99F")   #yellow
s.configure("tile2.TFrame", background="#41644A")   #green
s.configure("tileN.TFrame", background="#FF6D60")   #orange
s.configure("Horizontal.TFrame", background="#D14D72")   #pink
s.configure("Vertical.TFrame", background="#D21312")   #red
# Widgets -------------------------------

horizontal = ttk.Frame(root, width=600, height=50, style="Horizontal.TFrame")
horizontal.grid(row=0, column=0, columnspan=3, sticky="EW")
i = 1
j = 0
l = []
while i < 4:
    while j < 3:
        tileN = ttk.Frame(root, width=200, height=200, style="tileN.TFrame")
        tileN.grid(row=i, column=j, padx=1, pady=1, sticky="NEWS")
        tileN.grid_propagate(False)
        #coord = ttk.Label(tileN, text="Here")
        #coord.grid(row=1, column=1)
        frameList.append(tileN)
        j = j + 1
    j = 0
    i = i + 1

def draw(self):
    for tile in frameList:
        # Adding Image to Frame
        for widgets in tile.winfo_children():
            widgets.destroy()
        rand = random.randint(0,len(tileList)-1)
        img = ImageTk.PhotoImage(Image.open(tileList[rand].image))
        l.append(img)
        label = ttk.Label(tile, image=img)
        label.grid()

# Grid Config ---------------------------

#root.resizable(width=False, height=False)
root.bind("<Button-1>", draw)
root.mainloop()
