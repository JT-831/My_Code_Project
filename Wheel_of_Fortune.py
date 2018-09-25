# Wheel of Fortune, Random Name Selector

import random

def playergen():
    p_list = []
    count = 0
    
    num = int(input('Enter number of player: '))
    
    print('Enter Player(s) Name:')
    
    while count != num:
        count += 1
        name = input('{0}. '.format(count))
        p_list.append(name)

    return p_list

def shuffle_player(a): # function: shuffle the sequence of the player
    seq = random.sample(a, len(a))
    return seq

def play_game(player):
    
    game = True
    
    while game:
        if len(player) != 0:
            player = shuffle_player(player)
            index = random.randrange(0, len(player))
            print('Selected Player: {0}'.format(player[index]))
            del player[index]
            
            if len(player) != 0:
                next_player = input('Press <Enter> to show next player or any letter to add new player: ' + '\n')
                if next_player == '':
                    game = True
                else:
                    count = 0
                    num = int(input('Enter number of new player(s): '))
                    print('Enter New Player(s) Name:')
                    while count != num:
                        count += 1
                        name = input('{0}. '.format(count))
                        player.append(name)
                    game = True
        else:
            print('End of Program !')
            game = False

def main():
    player = playergen()
    play_game(player)
    
main()
