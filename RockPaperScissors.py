import random
def play():
    # game gunting batu kertas with computer
    user = input("'r for rock, 'p' for paper, 's' for scissorst: ").lower() # input r,p,s for user to play with the computer
    computer = random.choice(['r','p','s']) # random for computer to choice r,p,s
    print(computer)
    print(is_win)
    if user == computer:
        return 'It\'s a tie' # misalnya user dan computer memilih yang sama maka dia sama 
    
       # r>s, s>p, p>r

    if is_win(user, computer): # jika player atau computer  
        return'you won!'
    
    return 'you lost'

def is_win (player, musuh):
    #return true if player wins
    #r>s,s>p,p>r
    if(player == 'r' and musuh == 's') or (player == 's' and musuh == 'p') or (player == 'p' and musuh == 'r'): #
        return True
    
print(play())    