
import tkinter as tk
import csv

from Zone import StrikeZone
from Report import GameReport
from GameState import GameState
from ButtonWindow import ButtonWindow
from util import determineCode


# get game information
# home_team = input('Enter the name of the home team:')
# away_team = input('Enter the name of the away team:')
home_team = 'Miami University'
away_team = 'Kent State University'

# game state 
state = GameState()

# variable to keep track of current pitch
current_pitch = None

# dictionary of button bindings
# keys relate to the text of the buttons
pitch_colors = {
    'Strike Looking': 'Red',
    'Strike Swinging': 'Red',
    'Strike Swinging Ball': 'Red',
    'Foul Ball': 'Red',
    'Foul Out': 'Red',

    'Ball': 'Green',
    'Walk': 'Green',
    'Hit By Pitch': 'Green',
    'Wild Pitch': 'Green',

    'Single': 'Blue',
    "Single, Fielder's Choice": 'Blue',
    'Double': 'Blue',
    'Triple': 'Blue',
    'Home Run': 'Blue' ,

    'Ground Out':'Purple',
    'Fly Out':'Purple',
    'Pop Out':'Purple',
    'Line Out':'Purple',
    'Sac Fly':'Purple',
    'Double Play':'Purple',
    'Triple Play':'Purple',
    'Force Out':'Purple',

    'Bunt': 'Yellow',
    'Sac Bunt': 'Yellow',
    'Bunt Out (not sac)': 'Yellow',
    'Bunt Foul': 'Yellow',
    'Bunt no contact': 'Yellow'
}

# base position codes for 3-tuple of binary values
base_position_codes = {
    (0,0,0): 'Empty',
    (1,0,0): '1B',
    (0,1,0): '2B',
    (0,0,1): '3B',
    (1,1,0): '1B/2B',
    (0,1,1): '2B/3B',
    (1,0,1): '1B/3B',
    (1,1,1): 'BL'
}

# keep track of pitches as a list of dictionaries
pitches = []

# keep track of recent states (to be able to undo)
state_cache = []

base = tk.Tk()

# create windows
sz = StrikeZone(400,600,base,pitches)
gr = GameReport(base, pitches)
bw = ButtonWindow(base) 

def saveData(event):
    global pitches
    fname = gr.getFilename()
    if fname == '':
        fname = 'game.csv'
    with open(fname, 'w', newline='') as f:
        if len(pitches) > 0:
            writer = csv.DictWriter(f, fieldnames=pitches[0].keys())
            writer.writeheader()
            for pitch in pitches:
                writer.writerow(pitch)
    


def recordPitchLocation(event):
    global current_pitch
    # get event details
    x, y = event.x, event.y

    # ASSUMPTION: The strike zone is properly scaled
    # Math may be off by a little bit during this whole thing but only a few pixels probably

    # get zone coordinates
    x1, y1, x2, y2 = sz.getZoneCoords()

    # calculate scaled coordinates
    # use the width of the zone to determine the scale 
    zone_width = x2 - x1
    scale_factor = 100 / zone_width
    rel_x = round((x - x1) * scale_factor) # subtract the margin. 0 should be the left side of zone
    rel_y = round((y - y1) * scale_factor)

    current_pitch = {'x': rel_x, 'y': rel_y}

    
    # draw pitch 
    sz.drawPitch(x, y)


def recordPitchResult(event):
    global state, current_pitch

    # get button text
    text = event.widget['text']

    color = pitch_colors[text]

    # determine code
    code = determineCode(text, state)

    current_pitch['pitch_result'] = code
    

    # color pitch in gui
    sz.colorPitch(color)

def submitPitch(event):
    global current_pitch, state, pitches

    if current_pitch is None:
        return

    # add state to cache
    state_cache.append(state.copy())

    # get base positions
    b1 = bw.basePositions[0].get()
    b2 = bw.basePositions[1].get()
    b3 = bw.basePositions[2].get()
    bcode = base_position_codes[(b1,b2,b3)]

    # see if there was a steal
    if bw.stealBase.get() > 0:
        baseCodes = {1:'OUT', 2:'2B', 3:'3B', 4:'H'}
        current_pitch['stolen_base'] = baseCodes[bw.stealBase.get()] 
        current_pitch['steal_number']= bw.stealNumber.get() 
        # reset the steal base
        bw.stealBase.set(0)
    else: 
        current_pitch['stolen_base'] = ''
        current_pitch['steal_number']= ''

    # get pitch type
    pitchTypeCodes = {0:'', 1:'OFF'}
    pitchType = pitchTypeCodes[bw.pitchType.get()]
    bw.pitchType.set(0)


    # get runs
    runs = bw.runInput.get()
    bw.runInput.delete(0, 'end')
    bw.runInput.insert(0, 0)

    # fill pitch object
    current_pitch['base_position'] = bcode
    current_pitch['pitcher'] = gr.getPitcherNumber()
    current_pitch['batter'] = gr.getBatterNumber()
    current_pitch['balls'] = state.balls
    current_pitch['strikes'] = state.strikes
    current_pitch['outs'] = state.outs
    current_pitch['pitch_number'] = state.pitch_number
    current_pitch['inning'] = state.inning
    current_pitch['resulting_runs'] = runs
    current_pitch['at_bat'] = gr.getAwayTeam() if state.inning_top else gr.getHomeTeam()
    current_pitch['pitching_team'] = gr.getHomeTeam() if state.inning_top else gr.getAwayTeam()
    current_pitch['pitch_type'] = pitchType

    state.pitch_number += 1
    pitches.append(current_pitch)

    # update game state
    state.base_position = bcode
    state.updateGameState(current_pitch['pitch_result'])
    if current_pitch['stolen_base'] == 'OUT':
        print('called out')
        state.cs()

    # update game report window
    updateGameReport(state)

    # update zone window
    sz.removePitch()

    # add to previous pitch list
    gr.addPitch(current_pitch)

    # if there's a new inning or batting team, reset the base positions
    if current_pitch['at_bat'] != (gr.getAwayTeam() if state.inning_top else gr.getHomeTeam()):
        for base in bw.basePositions:
            base.set(0)

    current_pitch = None

def updateGameReport(state):
    # global home_team, away_team
    # gr.updateTitleLabel(home_team, away_team)
    gr.updateStateLabel(state.inning, state.outs, state.balls, state.strikes)

def undoPitch(event):
    global state
    # remove last pitch
    state = state_cache.pop()
    pitches.pop()
    sz.undoPitch
    gr.undoPitch()
    updateGameReport(state)

def main():

    updateGameReport(state)

    # bind events
    base.bind('<Configure>', sz.resize)
    base.bind('<Button-1>', recordPitchLocation)
    gr.undoButton.bind('<Button-1>', undoPitch)
    gr.saveButton.bind('<Button-1>', saveData)

    # binding buttons
    for button in bw.strikeInputs:
        button.bind('<Button-1>', recordPitchResult)
    for button in bw.ballInputs:
        button.bind('<Button-1>', recordPitchResult)
    for button in bw.hitInputs:
        button.bind('<Button-1>', recordPitchResult)
    for button in bw.outInputs:
        button.bind('<Button-1>', recordPitchResult)
    for button in bw.buntInputs:
        button.bind('<Button-1>', recordPitchResult)

    bw.window.bind('<Return>', submitPitch)
    bw.submitButton.bind('<Button-1>', submitPitch)

    base.attributes('-alpha', 0.3)
    base.mainloop()


if __name__ == '__main__':
    main()