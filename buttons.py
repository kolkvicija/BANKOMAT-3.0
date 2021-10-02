from tkinter import *

FONT = ("Courier New", 10, "bold")
LIGHT_BLUE = "#abd2fa"
DARK_BLUE = "#7692ff"
NUM_FONT = ("Courier New", 13, "bold")


class NumBtn:
    def __init__(self, win, br, r, c, com):
        self.win = win
        self.b1 = br
        self.r = r
        self.com = com
        self.c = c
        Button(master=win,
               text=br,
               bg="#7692ff",
               fg="white",
               padx=15,
               pady=15,
               highlightthickness=0,
               font = NUM_FONT,
               command=com).grid(row=r,
                                 column=c,
                                 pady=5,
                                 padx=5)


class Banka:
    def __init__(self, naziv, row, column, c):
        self.naziv = naziv
        self.row = row
        self.column = column
        self.c = c
        Button(text=naziv,
               height=3,
               width=15,
               font=FONT,
               padx=10,
               pady=10,
               highlightthickness=0,
               bg=DARK_BLUE,
               fg="white",
               command=c).grid(row=row,
                               column=column,
                               pady=5,
                               padx=5)
