
def determineCode(button_text, state):

    if button_text == 'Strike Looking':
        if state.strikes == 2:
            result = 'KL'
        else:
            result = 'STRIKE'

    elif button_text == 'Strike Swinging':
        if state.strikes == 2:
            result = 'KS'
        else:
            result = 'S/M'

    elif button_text == 'Strike Swinging Ball':
        if state.strikes == 2:
            result = 'KS'
        else:
            result = 'SSB'

    elif button_text == 'Foul Ball':
        result = 'FOUL'

    elif button_text == 'Foul Out':
        result = 'FOUL/O'

    elif button_text == 'Ball':
        result = 'BALL'

    elif button_text == 'Hit By Pitch':
        result = 'HBP'

    elif button_text == 'Wild Pitch':
        result = 'WP'

    elif button_text == 'Walk':
        result = 'W'

    elif button_text == 'Single':
        result = 'S'

    elif button_text == "Single, Fielder's Choice":
        result = 'S/FC'

    elif button_text == 'Double':
        result = '2B'
        
    elif button_text == 'Triple':
        result = 'TR'

    elif button_text == 'Home Run':
        result = 'HR'

    elif button_text == 'Ground Out':
        result = 'GO' 

    elif button_text == 'Fly Out':
        result = 'FO' 

    elif button_text == 'Pop Out':
        result = 'PO' 

    elif button_text == 'Line Out':
        result = 'LO' 

    elif button_text == 'Sac Fly':
        result = 'SacF' 

    elif button_text == 'Double Play':
        result = 'DP' 

    elif button_text == 'Triple Play':
        result = 'TP' 

    elif button_text == 'Force Out':
        result = 'FP' 

    elif button_text == 'Bunt':
        result = 'B'

    elif button_text == 'Sac Bunt':
        result = 'SacB'

    elif button_text == 'Bunt Out (not sac)':
        result = 'B/O'

    elif button_text == 'Bunt Foul':
        result = 'B/FOUL'

    elif button_text == 'Bunt no contact':
        result = 'B/M'

    return result


