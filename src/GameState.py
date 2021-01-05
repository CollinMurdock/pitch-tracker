

class GameState:

    def __init__(self):
        self.inning = 1
        self.inning_top = True
        self.strikes = 0
        self.balls = 0
        self.outs = 0
        self.home_score = 0
        self.away_score = 0
        self.pitch_number = 1
        self.base_position = 'Empty'


    def copy(self):
        result = GameState()
        result.inning = self.inning
        result.inning_top = self.inning_top 
        result.strikes = self.strikes 
        result.balls = self.balls 
        result.outs = self.outs 
        result.home_score = self.home_score 
        result.away_score = self.away_score 
        result.pitch_number = self.pitch_number 
        result.base_position = self.base_position

        return result


    def updateGameState(self, code):

        if code in ['STRIKE', 'S/M', 'KS', 'KL', 'SSB', 'B/M']:
            self.strike()

        if code in ['FOUL', 'B/FOUL']:
            self.foul()
                
        elif code == 'BALL':
            self.ball()

        elif code in ['S', '2B', 'TR', 'HR', 'B']:
            self.hit()

        elif code in ['W', 'HBP']:
            self.walk()

        elif code in ['GO', 'FO', 'LO', 'PO', 'SacF', 'FP', 'S/FC', 'SacB', 'B/O']:
            self.out()

        elif code == 'DP':
            self.dp()

        elif code == 'TP':
            self.tp()



    def strike(self):
        # update state for a strike
        if self.strikes == 2: 
            self.out()
        else:
            self.strikes += 1

    def foul(self):
        if self.strikes < 2:
            self.strikes += 1

    def ball(self):
        if self.balls == 3:
            self.balls = 0
            self.strikes = 0
        else:
            self.balls += 1

    def hit(self):
        self.balls = 0
        self.strikes = 0

    def walk(self): 
        self.balls = 0
        self.strikes = 0

    def out(self):
        self.balls = 0
        self.strikes = 0

        if self.outs == 2:
            if self.inning_top:
                self.inning_top = False
            else: 
                self.inning_top = True
                self.inning += 1
            self.outs = 0
        else:
            self.outs += 1
    
    def dp(self):
        if self.strikes == 2:
            self.out()
        else:
            self.out()
            self.out()

    def tp(self):
        if self.strikes == 0:
            self.out()
            self.out()
            self.out()
        elif self.strikes == 1:
            self.out()
            self.out()
        else:
            self.out()
