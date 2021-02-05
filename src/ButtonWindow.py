
import tkinter as tk

class ButtonWindow():

    def __init__(self, root):

        self.window = tk.Toplevel(root)

        # frame for all buttons
        self.buttonFrame = tk.Frame(self.window)
        self.buttonFrame.pack()

        # frame for pitch type
        self.pitchTypeInputFrame = tk.Frame(self.buttonFrame)
        self.pitchTypeInputFrame.pack()
        self.pitchTypeInputs = [] # list of all strike inputs
        self.pitchType = tk.IntVar()
        self.createPitchTypeInputs()

        # frame for strikes
        self.strikeInputFrame = tk.Frame(self.buttonFrame)
        self.strikeInputFrame.pack()
        self.strikeInputs = [] # list of all strike inputs
        self.createStrikeInputs()

        # frame for balls 
        self.ballInputFrame = tk.Frame(self.buttonFrame)
        self.ballInputFrame.pack()
        self.ballInputs = [] # list of all ball inputs
        self.createBallInputs()

        # frame for hits
        self.hitInputFrame = tk.Frame(self.buttonFrame)
        self.hitInputFrame.pack()
        self.hitInputs = [] # list of all ball inputs
        self.createHitInputs()

        # frame for bunts 
        self.buntInputFrame = tk.Frame(self.buttonFrame)
        self.buntInputFrame.pack()
        self.buntInputs = [] # list of all ball inputs
        self.createBuntInputs()

        # frame for ball in play outs 
        self.outInputFrame = tk.Frame(self.buttonFrame)
        self.outInputFrame.pack()
        self.outInputs = [] # list of all ball inputs
        self.createOutInputs()

        # frame for steal 
        self.stealInputFrame = tk.Frame(self.buttonFrame)
        self.stealInputFrame.pack()
        self.stealInputs = [] # list of all ball inputs
        self.stealBase = tk.IntVar()
        self.createStealInputs()

        # frame for entering new base positions
        self.basePositionInputFrame = tk.Frame(self.buttonFrame)
        self.basePositionInputFrame.pack()
        self.basePositions = [] # list of all ball inputs
        self.createBasePositionInputs()

        # frame for entering runs batted in
        self.runInputFrame = tk.Frame(self.buttonFrame)
        self.runInputFrame.pack()
        self.runInput = None # list of all ball inputs
        self.createRunInputs()


        # submit button 
        self.submitButton = tk.Button(self.buttonFrame, text='Submit Pitch')
        self.submitButton.pack()


    def createPitchTypeInputs(self):
        text = 'Pitch Type'
        lab = tk.Label(self.pitchTypeInputFrame, text=text, font='bold')
        lab.pack(side=tk.TOP)

        # create radio button for pitch type 
        changeup = tk.Radiobutton(self.pitchTypeInputFrame, text='Changeup', variable=self.pitchType, value=1)
        changeup.pack(side=tk.LEFT)
        self.pitchTypeInputs.append(changeup)

    def createStrikeInputs(self):
        text = 'Strikes'
        lab = tk.Label(self.strikeInputFrame, text=text, font='bold')
        lab.pack()
        texts = ['Strike Looking', 'Strike Swinging', 'Strike Swinging Ball', 'Foul Ball', 'Foul Out']
        for text in texts:
            b = tk.Button(self.strikeInputFrame, text=text)
            self.strikeInputs.append(b)
            b.pack(side=tk.LEFT)


    def createBallInputs(self):
        text = 'Balls'
        lab = tk.Label(self.ballInputFrame, text=text, font='bold')
        lab.pack()
        texts = ['Ball', 'Hit By Pitch', 'Walk', 'Wild Pitch']
        for text in texts:
            b = tk.Button(self.ballInputFrame, text=text)
            self.ballInputs.append(b)
            b.pack(side=tk.LEFT)

    def createHitInputs(self):
        text = 'Hits'
        lab = tk.Label(self.hitInputFrame, text=text, font='bold')
        lab.pack()
        texts = ['Single', "Single, Fielder's Choice", 'Double', 'Triple', 'Home Run']
        for text in texts:
            b = tk.Button(self.hitInputFrame, text=text )
            self.hitInputs.append(b)
            b.pack(side=tk.LEFT)

    def createBuntInputs(self):
        text = 'Bunts'
        lab = tk.Label(self.buntInputFrame, text=text, font='bold')
        lab.pack()
        texts = ['Bunt', 'Sac Bunt', 'Bunt Out (not sac)', 'Bunt Foul', 'Bunt no contact']
        for text in texts:
            b = tk.Button(self.buntInputFrame, text=text )
            self.buntInputs.append(b)
            b.pack(side=tk.LEFT)
            
    def createOutInputs(self):
        text = 'Ball in Play Outs'
        lab = tk.Label(self.outInputFrame, text=text, font='bold')
        lab.pack()
        texts = ['Ground Out', 'Fly Out','Pop Out','Line Out','Sac Fly','Double Play','Triple Play','Force Out']
        for text in texts:
            b = tk.Button(self.outInputFrame, text=text )
            self.outInputs.append(b)
            b.pack(side=tk.LEFT) 
    
    def createStealInputs(self):
        text = 'Stolen Base'
        lab = tk.Label(self.stealInputFrame, text=text, font='bold')
        lab.pack(side=tk.TOP)

        # create radio button for base
        base2 = tk.Radiobutton(self.stealInputFrame, text='Second Base', variable=self.stealBase, value=2)
        base2.pack(side=tk.LEFT)
        self.stealInputs.append(base2)
        base3 = tk.Radiobutton(self.stealInputFrame, text='Third Base', variable=self.stealBase, value=3)
        base3.pack(side=tk.LEFT)
        self.stealInputs.append(base3)
        base4 = tk.Radiobutton(self.stealInputFrame, text='Home Base', variable=self.stealBase, value=4)
        base4.pack(side=tk.LEFT)
        self.stealInputs.append(base4)

        # create out option 
        out = tk.Radiobutton(self.stealInputFrame, text='Called Out', variable=self.stealBase, value=1)
        out.pack(side=tk.LEFT)
        self.stealInputs.append(out)

        # create label
        text = 'Player Number'
        lab = tk.Label(self.stealInputFrame, text=text)
        lab.pack()

        self.stealNumber = tk.Spinbox(self.stealInputFrame, from_=0, to=99)
        self.stealNumber.pack()


    def createBasePositionInputs(self):
        text = 'Base Position'
        lab = tk.Label(self.basePositionInputFrame, text=text, font='bold')
        lab.pack()

        bvar1 = tk.IntVar()
        bvar2 = tk.IntVar()
        bvar3 = tk.IntVar()

        # use checkboxes 
        b1 = tk.Checkbutton(self.basePositionInputFrame, text='First Base', onvalue=1, offvalue=0, variable=bvar1)
        b1.pack()
        b2 = tk.Checkbutton(self.basePositionInputFrame, text='Second Base', onvalue=1, offvalue=0, variable=bvar2)
        b2.pack()
        b3 = tk.Checkbutton(self.basePositionInputFrame, text='Third Base', onvalue=1, offvalue=0, variable=bvar3)
        b3.pack()

        self.basePositions.append(bvar1)
        self.basePositions.append(bvar2)
        self.basePositions.append(bvar3)

    def createRunInputs(self):
        text = 'Runs batted in'
        lab = tk.Label(self.runInputFrame, text=text, font='bold')
        lab.pack()

        self.runInput = tk.Spinbox(self.runInputFrame, from_=0, to=99)
        self.runInput.pack()

    
