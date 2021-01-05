
import tkinter as tk

class StrikeZone:

    def __init__(self, height, width, root, pitchList):

        self.C = tk.Canvas(root, bg='#0d1524', height =height, width=width)
        self.C.pack()

        # strike_zone rectangle, initially none
        self.strike_zone = None
        # strike_zone coordinates, initially 0, filled on resize
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        # pitch circle drawn
        self.pitch = None
        self.radius = 10
        self.ball_color = 'White'



    def resize(self, event):
        width, height = self.C.winfo_width(), self.C.winfo_height()
        self.drawStrikeZone(width, height)


    def drawStrikeZone(self, win_width, win_height, min_margin = 50, ratio=1.5):

        # get largest possible width
        max_width = win_width - 2 * min_margin # 200
        # get largest possible height 
        max_height = win_height - 2 * min_margin # 200

        # arguments needed for create_rectangle
        # if the window size were perfect, these would be correct
        self.x1 = min_margin 
        self.y1 = min_margin 
        self.x2 = win_width - min_margin 
        self.y2 = win_height - min_margin 

        if max_width * ratio > max_height: 
            # too wide      
            w = round(max_height / ratio) 
            self.x1 = round((win_width - w) / 2) 
            self.x2 = win_width - self.x1 
        else: # to tall
            h = round(max_width * ratio)
            self.y1 = round((win_height - h) / 2) 
            self.y2 = win_height - self.y1

        if self.strike_zone is not None:
            self.C.delete(self.strike_zone)
        self.strike_zone = self.C.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline='#bdbdbd')

    
    def getZoneCoords(self):
        return (self.x1, self.y1, self.x2, self.y2)


    def drawPitch(self, x, y):
        # redraw pitch circle
        if self.pitch is not None:
            self.C.delete(self.pitch)
        radius = self.radius
        self.pitch = self.C.create_oval(x-radius, y-radius, x+radius, y+radius, outline='black', fill=self.ball_color)

    def colorPitch(self, color):
        # color the pitch
        self.C.itemconfig(self.pitch, fill=color) 

    def removePitch(self):
        self.C.delete(self.pitch)

    def undoPitch(event):
        if self.pitch is not None:
            self.C.delete(self.pitch)