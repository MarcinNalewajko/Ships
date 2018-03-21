import os
import copy
columns=['A','B','C','D','E','F','G','H','I','J']
rows=['1','2','3','4','5','6','7','8','9','10']
base_matrix=[['\ ',' A ',' B ',' C ',' D ',' E ',' F ',' G ',' H ',' I ',' J '],
['1 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['2 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['3 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['4 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['5 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['6 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['7 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['8 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['9 ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ '],
['10',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ',' ~ ']]
matrix=copy.deepcopy(base_matrix)
player1_board=copy.deepcopy(base_matrix)
player2_board=copy.deepcopy(base_matrix)
player1_game=copy.deepcopy(base_matrix)
player2_game=copy.deepcopy(base_matrix)
list_of_ships=[1]
counter1=0
counter2=0
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def prt():
    for i in range (0,len(matrix)):
        print(''.join(matrix[i]))
def ship(size):   
    prt()
    dir=0
    print('\n','\n','\n',Place ship which will have have size of '+ str(size)+  ' points.')
    if size>1:    
        while not (dir=='row' or dir=='col'):
            dir=input('What direction ship will have: col for columns row for rows: ')
            #dir='row'
            repeat=1
    else:
        dir='row'
        repeat=1
    while repeat:
        high_repeat=0
        position=(input('Insert position in format letter of column(Capital) and number of row i.e. B5: '))
        #position='A1'
        try:
            lines=int(position[1:])
            cols=(columns.index(position[0])+1)
            if (position[0] in  columns) and(position[1:]in rows):
                if dir == 'row':
                    for x in range (0,size):
                        if matrix[lines][(cols+x)]==' 0 ':
                            high_repeat=1
                            print('Your ship will cross with another one put it elsewhere')
                        else:
                            repeat=0
                    if high_repeat==1:
                        repeat=1
                    else:
                        repeat=0
                elif dir == 'col':
                    for x in range (0,size):
                        if matrix[(lines+x)][(cols)]==' 0 ':
                            high_repeat=1
                            print('Your ship will cross with another one put it elsewhere')
                        else:
                            repeat=0
                    if high_repeat==1:
                        repeat=1
                    else:
                        repeat=0
            else:
                repeat=1
                print('Mistake in position. Please put correct one.')
        except ValueError:
            repeat=1
            print('Mistake in position. Please put correct one.')
        except IndexError:
            repeat=1
            print('Ship not on playground. Please put correct position.')
    if dir == 'row':
        for x in range (0,size):
            matrix[lines][(cols+x)]=' 0 '
    elif dir == 'col':
        for x in range (0,size):
            matrix[(lines+x)][(cols)]=' 0 ' 
    cls()

def Title(playernumber):
    print('            PLAYER ',str(playernumber),'\n''\n''\n')

def player1_set():
    global player1_board
    global matrix
    global base_matrix
    for elem in list_of_ships:    
        Title(1)
        ship(elem)
    player1_board=copy.deepcopy(matrix)
def player2_set():
    global matrix
    global base_matrix
    global player2_board
    matrix=copy.deepcopy(base_matrix)
    for elem in list_of_ships:    
        Title(2)
        ship(elem)
    player2_board=copy.deepcopy(matrix)
def doubleboard():
    print('            PLAYER 1'+'                                                            '+ 'PLAYER 2','\n','\n','\n')
    for i in range (0,11):
        print(''.join(player1_game[i])+'                                    '+''.join(player2_game[i]))
def fight_for_2():
    global matrix
    global base_matrix
    global player2_board
    global player1_board
    global player1_game
    global player2_game
    global winner
    counter1=0
    counter2=0
    player=1
    repeat=1
    print(player2_board)
    while (counter1<sum(list_of_ships)) and (counter2<sum(list_of_ships)):
        while repeat==1:
            cls()
            doubleboard()
            if player==1:
                repeat=1
                print('\n','\n','\n','Player '+str(player)+' is shooting now!')
                position=(input('Insert position in format letter of column(Capital) and number of row i.e. B5: '))
                #position='A2'
                try:
                    lines=int(position[1:])
                    cols=(columns.index(position[0])+1) 
                    if player2_board[lines][cols]==' 0 ':
                        player2_board[lines][cols]=' X '
                        player1_game[lines][cols]=' X '
                        repeat=1
                        counter1+=1
                        player=2
                        if counter1==sum(list_of_ships):
                            repeat=0
                            winner=1
                            break
                        else:
                            cls()
                            doubleboard()
                    elif player2_board[lines][cols]==' ~ ':
                        player2_board[lines][cols]=' * '
                        player1_game[lines][cols]=' * '
                        repeat=1
                        player=2
                        cls()
                        doubleboard()
                    else:
                        print('You already have tried to hit this place, try something else.')
                        repeat=1
                except ValueError:
                    repeat=1
                    print('Mistake in position. Please put correct one.')
                except IndexError:
                    repeat=1
                    print('You have tried to shot something not on playground. Please put correct position.')
            
            if player==2:
                repeat=1
                print('\n','\n','\n','Player '+str(player)+' is shooting now!')
                position=(input('Insert position in format letter of column(Capital) and number of row i.e. B5: '))
                #position='A1'
                try:
                    lines=int(position[1:])
                    cols=(columns.index(position[0])+1) 
                    if player1_board[lines][cols]==' 0 ':
                        player1_board[lines][cols]=' X '
                        player2_game[lines][cols]=' X '
                        repeat=1
                        counter2+=1
                        player=1
                        if counter2==sum(list_of_ships):
                            repeat=0
                            winner=2
                            break
                        else:
                            cls()
                            doubleboard()
                    elif player1_board[lines][cols]==' ~ ':
                        player1_board[lines][cols]=' * '
                        player2_game[lines][cols]=' * '
                        repeat=1
                        player=1
                        cls()
                        doubleboard()
                    else:
                        print('You already have tried to hit this place, try something else.')
                        repeat=1
                except ValueError:
                    repeat=1
                    print('Mistake in position. Please put correct one.')
                except IndexError:
                    repeat=1
                    print('You have tried to shot something not on playground. Please put correct position.')
        else:
            repeat=1
    cls()
def game_for_2():
    cls()
    player1_set()
    player2_set()
    fight_for_2()
    print('The winner is: player '+str(winner))
    end=input('Press enter to go to main menu')
    menu()
def legend():
    cls()
    print('~  symbol of water')
    print('O  element of ship')
    print('X  hit')
    print('*  miss')
    end=input('Press enter to go to main menu')
    menu()
def menu():
    do_in_menu=0
    cls()
    print('',
    '      SSSSSSSSS         H     H        I        PPPPPPPP      SSSSSSSSS ','\n',
    '    SSS                 H     H        I        P      P    SSS','\n',
    '    SSS                 H     H        I        P      P    SSS','\n',
    '      SSSSSSSS          HHHHHHH        I        PPPPPPPP      SSSSSSSS','\n',
    '            SSS         H     H        I        P                   SSS','\n',
    '            SSS         H     H        I        P                   SSS','\n',
    '    SSSSSSSSSS          H     H        I        P           SSSSSSSSSS','\n',
    '\n','\n','\n','\n','\n','1. Start Game for 2 players','\n','2. Legend of symbols'
    ,'\n','\n','\n')
    
    while not (do_in_menu=='1' or do_in_menu=='2'):
        do_in_menu=input('What do you want to do now: ')
        if not (do_in_menu=='1' or do_in_menu=='2'):
            print('This option is not available')
        if (do_in_menu=='1'):
            game_for_2()
        if (do_in_menu=='2'):
            legend()

cls()
menu()
#game_for_2()
