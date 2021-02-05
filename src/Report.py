
import tkinter as tk

class GameReport:

    def __init__(self, root, pitchList):

        self.window = tk.Toplevel(root)

        # declare labels
        self.titleLabel = None
        self.countLabel = None

        # frame that contains the game information
        self.reportFrame = tk.Frame(self.window)
        self.reportFrame.pack()

        # frame that contains inputs
        self.inputFrame = tk.Frame(self.window)
        self.inputFrame.pack()
        self.createInputs()

        # frame that contains previous pitches
        self.prevPitchFrame = tk.Frame(self.window)
        self.prevPitchFrame.pack()
        # create label
        self.prevPitchTitleLabel = tk.Label(self.prevPitchFrame, text='Recent Pitches')
        self.prevPitchTitleLabel.pack()
        # undo button
        self.undoButton = tk.Button(self.prevPitchFrame, text='Undo Pitch')
        self.undoButton.pack(side=tk.BOTTOM)
        # empty list of pitches to keep track of
        self.pitchLabels = []


    def updateTitleLabel(self, homeTeam, awayTeam):
        title_str = homeTeam +' - ' + awayTeam
        if self.titleLabel is not None:
            self.titleLabel['text'] = title_str
        else:
            self.titleLabel = tk.Label(self.reportFrame, text=title_str)
        self.titleLabel.pack()

    
    def updateStateLabel(self, inning, outs, balls, strikes):
        text = 'Inning: ' + str(inning)
        text += '\nOuts: ' + str(outs) 
        text += '\nCount: ' + str(balls) + '-' + str(strikes) 
        if self.countLabel is not None:
            self.countLabel['text'] = text
        else:
            self.countLabel = tk.Label(self.reportFrame, text=text)
        self.countLabel.pack()

    def addPitch(self, pitch_data):
        # param pitch_data: a dict of information about the pitch (see main.py)

        # if 10 pitches already there, remove the first
        if len(self.pitchLabels) == 10: 
            l = self.pitchLabels.pop(0)
            l.destroy()

        text = 'Outs: ' + str(pitch_data['outs'])
        text += '\tCount: ' + str(pitch_data['balls']) + ' - ' + str(pitch_data['strikes'])
        text += '\tBases: ' + pitch_data['base_position']
        text += '\tResult: ' + pitch_data['pitch_result']
        label = tk.Label(self.prevPitchFrame, text=text)
        self.pitchLabels.append(label)
        label.pack()

    def undoPitch(self):
        self.pitchLabels.pop().destroy()

    def createInputs(self):

        # save button
        self.saveButton = tk.Button(self.window, text='Save Data')
        self.saveButton.pack()

        # team inputs
        self.home_input_frame = tk.Frame(self.window)
        self.home_input_frame.pack()
        l = tk.Label(self.home_input_frame, text="Home Team Code:")
        l.pack( side = tk.LEFT)
        self.home_team = tk.Entry(self.home_input_frame, bd =5)
        self.home_team.pack(side = tk.RIGHT)

        # team inputs
        self.away_team_inputs= tk.Frame(self.window)
        self.away_team_inputs.pack()
        l = tk.Label(self.away_team_inputs, text="Away Team Code:")
        l.pack( side = tk.LEFT)
        self.away_team = tk.Entry(self.away_team_inputs, bd =5)
        self.away_team.pack(side = tk.RIGHT)

        # filename input
        self.filename_input_frame = tk.Frame(self.window)
        self.filename_input_frame.pack()
        l = tk.Label(self.filename_input_frame, text="Filename (inlucding extension):")
        l.pack( side = tk.LEFT)
        self.filename = tk.Entry(self.filename_input_frame, bd =5)
        self.filename.pack(side = tk.RIGHT)

        # pitcher number input
        self.pitcher_input_frame = tk.Frame(self.window)
        self.pitcher_input_frame.pack()
        l = tk.Label(self.pitcher_input_frame, text="Pitcher Number")
        l.pack( side = tk.LEFT)
        self.pitcher_num = tk.Entry(self.pitcher_input_frame, bd =5)
        self.pitcher_num.pack(side = tk.RIGHT)

        # pitcher number input
        self.batter_input_frame = tk.Frame(self.window)
        self.batter_input_frame.pack()
        l = tk.Label(self.batter_input_frame, text="Batter Number")
        l.pack( side = tk.LEFT)
        self.batter_num = tk.Entry(self.batter_input_frame, bd =5)
        self.batter_num.pack(side = tk.RIGHT)

        


    def getPitcherNumber(self):
        return self.pitcher_num.get()

    def getBatterNumber(self):
        return self.batter_num.get()

    def getFilename(self):
        return self.filename.get()

    def getHomeTeam(self):
        return self.home_team.get()

    def getAwayTeam(self):
        return self.away_team.get()