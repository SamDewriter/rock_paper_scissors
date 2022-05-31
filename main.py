import random 

moves = ['R', 'P', 'S']
moves_id = {'R':'Rock', 'P':'Paper', 'S': 'Scissors'}
     
def get_player_selection():
    """Gets player selection and return it as action"""
    
    player_selection = input('Pick an option between R, P, or S: ')
    action = player_selection.upper()
    return action

def get_computer_selection():
    """Gets computer selection and return it as action"""

    computer_selection = random.choice(moves)
    action = computer_selection
    return action 
    
def determine_winner(player, computer):
    """Gets both player and computer selections and determine the winner
    
    Args:
        player (str)
        computer (str)
    """
    # R = moves[0], P = moves[1], S = moves[2]
    if player == moves[0] and computer == moves[2]:
        print('Player wins!')
    elif player == moves[2] and computer == moves[0]:
        print('CPU wins!')
    elif player == moves[2] and computer == moves[1]:
        print('Player wins!')
    elif player == moves[1] and computer == moves[2]:
        print('CPU wins!')
    elif player == moves[1] and computer == moves[0]:
        print('Player wins!')
    elif player == moves[0] and computer == moves[1]:
        print('CPU wins!')
    
while True:
    
    player = get_player_selection()
    computer = get_computer_selection()

    if player not in moves:
        print('Error! Choose an appropriate move and try again!')
        continue 
    
    elif player in moves:
        print(f'Player ({moves_id[player]}) : CPU ({moves_id[computer]})')
        
        if player == computer:
            print('It\'s a tie. Play again!')
        
        elif player != computer:
            print('Congratulations')
            determine_winner(player, computer)
        
        play_again = input('Do you want to play another game? ')
            
        if  play_again.lower() != 'y':
            break
