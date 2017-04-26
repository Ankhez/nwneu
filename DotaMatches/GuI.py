# -*- coding:utf-8 -*-
from Tkinter import *
import DotaMathes


class But_print(object):

    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "Печать"
        self.but.bind("<Button-1>", self.printer)
        self.but.pack()
        self.tex = Text(root, width = 150, font ="Verdana 12", wrap = WORD)
        self.tex.pack()

    def printer(self, event):
        for element in DotaMathes.Matches.parsewithpagination():
            self.tex.insert(END, '\n'+element)


root = Tk()
obj = But_print()
root.mainloop()

