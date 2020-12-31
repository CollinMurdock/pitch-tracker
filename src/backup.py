import tkinter as tk
import csv

pitch = None
strike_zone = None
ball_color = 'Red'
pitches = [] 
save_filename = 'game.csv'



base = tk.Tk()

base.rowconfigure(0, weight=1)
base.columnconfigure(0, weight=1)

# Set the original parameters
height = 500
width = 400
radius = 10
ratio = 1.5 # how much taller the zone is than wide

# these variables change depending on the size of the window
# will be filled with correct values on window creation
# needed for the recordPitch functionality (to know the scale)
zone_x1 = 0
zone_x2 = 0
zone_y1 = 0
zone_y2 = 0

# Build the basic gui
C = tk.Canvas(base, bg='#0d1524', height =height, width=width)
# C.create_text(width/2,30,fill="white",font="Times 20 bold",
                        # text="Strikezone Grid")


# create biggest rectangle with ratio 1 width by the argument while maintaining the min_margin
def drawStrikeZone(win_width, win_height, min_margin = 50, ratio=1.5):
    global strike_zone
    global x1 
    global x2 
    global y1 
    global y2

    # get largest possible width
    max_width = win_width - 2 * min_margin # 200
    # get largest possible height 
    max_height = win_height - 2 * min_margin # 200

    # arguments needed for create_rectangle
    # if the window size were perfect, these would be correct
    x1 = min_margin # 50
    y1 = min_margin # 50
    x2 = win_width - min_margin # 250
    y2 = win_height - min_margin # 250

    if max_width * ratio > max_height: # 300 > 200
        # too wide      
        w = round(max_height / ratio) # 133
        x1 = round((win_width - w) / 2) # 84
        x2 = win_width - x1 # 216
    else: # to tall
        h = round(max_width * ratio)
        y1 = round((win_height - h) / 2) 
        y2 = win_height - y1

    if strike_zone is not None:
        C.delete(strike_zone)
    strike_zone = C.create_rectangle(x1, y1, x2, y2, outline='#bdbdbd')

# C2 = tk.Canvas(base, bg='White', height =height, width=width)
# pt = Table(C2, dataframe=df, showtoolbar=True, showstatusbar=True)
# pt.show()

C.pack()


def recordClick(event):
    global df
    global pitch
    global ball_color
    global pitches
    global x1, x2, y1, y2

    # ASSUMPTION: The strike zone is properly scaled
    # Math may be off by a little bit during this whole thing but only a few pixels probably
    # window coordinates of lcick
    x, y = event.x, event.y

    # calculate scaled coordinates
    # use the width of the zone to determine the scale 
    zone_width = x2 - x1
    scale_factor = 100 / zone_width
    rel_x = round((x - x1) * scale_factor) # subtract the margin. 0 should be the left side of zone
    rel_y = round((y - y1) * scale_factor)

    pitches.append({'x': rel_x, 'y': rel_y}) 

    # redraw pitch circle
    if pitch is not None:
        C.delete(pitch)
    pitch = C.create_oval(x-radius, y-radius, x+radius, y+radius, outline='black', fill=ball_color)


def undoPitch(event):
    print('undoPitch')
    global pitches
    global pitch
    if pitch is not None:
        C.delete(pitch)

    pitches.pop()

    
# resize based on window
def resize(event):
    width, height = C.winfo_width(), C.winfo_height()
    drawStrikeZone(width, height)

def saveData():
    global pitches

    with open(save_filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['x', 'y'])
        writer.writeheader()
        for pitch in pitches:
            writer.writerow(pitch)
    
    base.destroy()

    
# base.attributes('-alpha', 0.3)

base.bind('<Button-1>', recordClick)
base.bind('<z>', undoPitch)
base.bind('<Configure>', resize)
base.protocol("WM_DELETE_WINDOW", saveData)


def sayHey(event):
    print('hey')

base2 = tk.Toplevel()
base2.bind('<Button-1>', sayHey)

base.mainloop()

