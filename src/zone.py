import tkinter as tk

class StrikeZone:


    # args:
    #   height  -   initial window height
    #   width   -   initial window width
    def __init__(self, width, height):

        # variables
        self.pitch = None
        self.strike_zone = None
        self.pitches = [] 
        self.radius = 10
        self.ratio = 1.5 # how much taller the zone is than wide

        # these variables change depending on the size of the window
        # will be filled with correct values on window creation
        # needed for the recordPitch functionality (to know the scale)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        # create window
        self.base = tk.Tk()

        self.base.rowconfigure(0, weight=1)
        self.base.columnconfigure(0, weight=1)

        # Build the basic gui
        self.C = tk.Canvas(self.base, bg='#0d1524', height =height, width=width)
        self.C.pack()

        # base.attributes('-alpha', 0.3)
        self.base.bind('<Button-1>', self.recordClick)
        self.base.bind('<z>', self.undoPitch)
        self.base.bind('<Configure>', self.resize)

        self.base.mainloop()

    def connect(self, widget, signal, event):
        widget.bind(signal, event)

    # create biggest rectangle with ratio 1 width by the argument while maintaining the min_margin
    def drawStrikeZone(self, win_width, win_height, min_margin = 50, ratio=1.5):

        # get largest possible width
        max_width = win_width - 2 * min_margin 
        # get largest possible height 
        max_height = win_height - 2 * min_margin 

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

    def recordClick(self, event):
        # ASSUMPTION: The strike zone is properly scaled
        # Math may be off by a little bit during this whole thing but only a few pixels probably
        # window coordinates of lcick
        x, y = event.x, event.y

        # calculate scaled coordinates
        # use the width of the zone to determine the scale 
        zone_width = self.x2 - self.x1
        scale_factor = 100 / zone_width
        rel_x = round((x - self.x1) * scale_factor) # subtract the margin. 0 should be the left side of zone
        rel_y = round((y - self.y1) * scale_factor)

        self.pitches.append({'x': rel_x, 'y': rel_y}) 

        # redraw pitch circle
        if self.pitch is not None:
            self.C.delete(self.pitch)
        radius = self.radius
        self.pitch = self.C.create_oval(x-radius, y-radius, x+radius, y+radius, outline='black', fill='White')

    def undoPitch(self, event):
        print('undoPitch')
        if self.pitch is not None:
            self.C.delete(self.pitch)

        self.pitches.pop()

    # resize based on window
    def resize(self, event):
        width, height = self.C.winfo_width(), self.C.winfo_height()
        self.drawStrikeZone(width, height)



    




