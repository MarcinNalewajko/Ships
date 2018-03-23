import os
import copy
global END
global WATER
global SHIP
global HIT
global MISS
global ship
global hit
global miss
global water
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
END="\033[1;m"
WATER="\33[1;34;46m"
SHIP="\33[1;30;47m"
HIT="\33[1;31;47m"
MISS="\33[1;31;46m"
#water=[WATER,' ~ ',END]
water=WATER+' ~ ' + END
ship=SHIP+' O ' + END
print(ship)
hit=HIT+' X '+ END
miss=MISS+' * '+ END
base_matrix = [
    ['\ ', ' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ', ' I ', ' J '],
    ['1 ', water, water, water, water, water, water, water, water, water, water],
    ['2 ', water, water, water, water, water, water, water, water, water, water],
    ['3 ', water, water, water, water, water, water, water, water, water, water],
    ['4 ', water, water, water, water, water, water, water, water, water, water],
    ['5 ', water, water, water, water, water, water, water, water, water, water],
    ['6 ', water, water, water, water, water, water, water, water, water, water],
    ['7 ', water, water, water, water, water, water, water, water, water, water],
    ['8 ', water, water, water, water, water, water, water, water, water, water],
    ['9 ', water, water, water, water, water, water, water, water, water, water],
    ['10', water, water, water, water, water, water, water, water, water, water]
    ]
player1_board = copy.deepcopy(base_matrix)
player2_board = copy.deepcopy(base_matrix)
player1_game = copy.deepcopy(base_matrix)
player2_game = copy.deepcopy(base_matrix)
list_of_ships = []
counter1 = 0
counter2 = 0

def hit_sound():
    os.system("aplay explosion.wav")


def miss_sound():
    os.system("aplay splash.wav")


def set_sound():
    os.system("aplay horn.wav")



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board_for_ship_set(size, matrix):
    for i in range(0, len(matrix)):
        print(''.join(matrix[i]))
    print('\n', '\n', '\n', 'Place ship which will have have size of '+ str(size)+  ' points.')


def check_columns(matrix, size, position, lines, cols):
    try:
        repeat = 0
        for x in range(0, size):
            if matrix[(lines + x)][(cols)] == ship:
                repeat = 1
                print('Your ship will cross with another one put it elsewhere')
            else:
                pass
    except IndexError:
        repeat = 1
        print('Ship not on playground. Please put correct position.')
    finally:
        return repeat


def check_rows(matrix, size, position, lines, cols):
    try:
        repeat = 0
        for x in range(0, size):
            if matrix[lines][(cols + x)] == ship:
                repeat = 1
                print('Your ship will cross with another one put it elsewhere')
            else:
                pass
                
    except IndexError:
        repeat = 1
        print('Ship not on playground. Please put correct position.')
    return repeat  


def print_ship(matrix, size, dir, lines, cols):
    if dir == 'row':
        for x in range(0, size):
            matrix[lines][(cols + x)] = ship
    elif dir == 'col':
        for x in range(0, size):
            matrix[(lines + x)][(cols)] = ship
    



def set_ship_direction(size):
    dir = 0
    if size > 1:
        while not (dir == 'row' or dir == 'col'):
            dir = input(
                'What direction ship will have: col for columns row for rows: ')
            # dir='row'
    else:
        dir = 'row'
    return dir


def check_ship_out_of_board(repeat, position, columns):
    try:
        lines = position[1:]
        cols = (columns.index(position[0]) + 1)    
    except ValueError:
        lines=0
        cols=0
        repeat = 1
        #print('Mistake in position. Please put correct one.')
    return [repeat, int(lines), int(cols)]

def check_col_row(matrix, size, position, lines, cols, dir):
    if (position[0] in columns) and(position[1:]in rows):
        if dir == 'row':
            repeat = check_rows(matrix, size, position, lines, cols)
        elif dir == 'col':
            repeat = check_columns(matrix, size, position, lines, cols)
    else:
        repeat = 1
        print('Mistake in position. Please put correct one.')
    return repeat


def ship_set(size,matrix):
    print_board_for_ship_set(size, matrix)
    dir = set_ship_direction(size)
    repeat = 1
    while repeat:
        position = (input('Insert position in format letter of column(Capital) and number of row i.e. B5: '))
        # position='A1'
        #TODO change to dictionary
        out_test=check_ship_out_of_board(repeat, position, columns)
        repeat = out_test[0]
        lines = out_test[1]
        cols = out_test[2]
        repeat = check_col_row(matrix, size, position, lines, cols, dir)       
    print_ship(matrix, size, dir, lines, cols)
    return matrix


def Title(playernumber):
    print('            PLAYER ', str(playernumber), '\n''\n''\n')


def player_set(list_of_ships, matrix, playernumber):
    for elem in list_of_ships:
        Title(playernumber)
        ship_set(elem, matrix)
        set_sound()
        cls()
    return matrix


def doubleboard():
    print('            PLAYER 1' +'                                                            ' + 'PLAYER 2', '\n', '\n', '\n')
    print(''.join(player1_game[0]) + '                                    ' + ''.join(player2_game[0]))
    for i in range(1, 11):
        print(player1_game[i][0]+''+WATER+''.join(player1_game[i][1:])+END+ '                                    ' + player2_game[i][0]+''+WATER+''.join(player2_game[i][1:])+END)


def fight_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns):
    counter1 = 0
    counter2 = 0
    player = 1
    repeat = 1
    print(player2_board)
    while (counter1 < sum(list_of_ships)) and (counter2 < sum(list_of_ships)):
        while repeat == 1:
            cls()
            doubleboard()
            if player == 1:
                repeat = 1
                print('\n', '\n', '\n', 'Player ' + str(
                    player) + ' is shooting now!')
                position = (
                    input('Insert position in format letter of column(Capital) and number of row i.e. B5: '))
                # position='A2'
                try:
                    lines = int(position[1:])
                    cols = (columns.index(position[0]) + 1)
                    if player2_board[lines][cols] == ship:
                        hit_sound()
                        player2_board[lines][cols] = hit
                        player1_game[lines][cols] = hit
                        repeat = 1
                        counter1 += 1
                        player = 2
                        if counter1 == sum(list_of_ships):
                            repeat = 0
                            winner = 1
                            break
                        else:
                            cls()
                            doubleboard()
                    elif player2_board[lines][cols] == water:
                        miss_sound()
                        player2_board[lines][cols] = miss
                        player1_game[lines][cols] = miss
                        repeat = 1
                        player = 2
                        cls()
                        doubleboard()
                    else:
                        print(
                            'You already have tried to hit this place, try something else.')
                        repeat = 1
                except ValueError:
                    repeat = 1
                    print('Mistake in position. Please put correct one.')
                except IndexError:
                    repeat = 1
                    print(
                        'You have tried to shot something not on playground. Please put correct position.')

            if player == 2:
                repeat = 1
                print('\n', '\n', '\n', 'Player ' + str(
                    player) + ' is shooting now!')
                position = (
                    input('Insert position in format letter of column(Capital) and number of row i.e. B5: '))
                # position='A1'
                try:
                    lines = int(position[1:])
                    cols = (columns.index(position[0]) + 1)
                    if player1_board[lines][cols] == ship:
                        player1_board[lines][cols] = hit
                        player2_game[lines][cols] = hit
                        repeat = 1
                        counter2 += 1
                        player = 1
                        if counter2 == sum(list_of_ships):
                            repeat = 0
                            winner = 2
                            break
                        else:
                            cls()
                            doubleboard()
                    elif player1_board[lines][cols] == water:
                        player1_board[lines][cols] = miss
                        player2_game[lines][cols] = miss
                        repeat = 1
                        player = 1
                        cls()
                        doubleboard()
                    else:
                        print(
                            'You already have tried to hit this place, try something else.')
                        repeat = 1
                except ValueError:
                    repeat = 1
                    print('Mistake in position. Please put correct one.')
                except IndexError:
                    repeat = 1
                    print(
                        'You have tried to shot something not on playground. Please put correct position.')
        else:
            repeat = 1
    cls()
    return winner


def game_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns,):
    cls()
    player1_board = player_set(list_of_ships, player1_board, 1)
    player2_board = player_set(list_of_ships, player2_board, 2)
    winner = fight_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)
    print('The winner is: player ' + str(winner),'\n','\n')
    end = input('Press enter to go to main menu')
    menu(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)


def legend():
    cls()
    print('~  symbol of water')
    print('O  element of ship')
    print('X  hit')
    print('*  miss')
    end = input('Press enter to go to main menu')
    menu(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)


def menu(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns):
    do_in_menu = 0
    cls()
    print('',
          '      SSSSSSSSS         H     H        I        PPPPPPPP      SSSSSSSSS ', '\n',
          '    SSS                 H     H        I        P      P    SSS', '\n',
          '    SSS                 H     H        I        P      P    SSS', '\n',
          '      SSSSSSSS          HHHHHHH        I        PPPPPPPP      SSSSSSSS', '\n',
          '            SSS         H     H        I        P                   SSS', '\n',
          '            SSS         H     H        I        P                   SSS', '\n',
          '    SSSSSSSSSS          H     H        I        P           SSSSSSSSSS', '\n',
          '\n', '\n', '\n', '\n', '\n', '1. Start Game for 2 players', '\n', '2. Legend of symbols', '\n', '\n', '\n')

    while not (do_in_menu == '1' or do_in_menu == '2'):
        do_in_menu = input('What do you want to do now: ')
        if not (do_in_menu == '1' or do_in_menu == '2'):
            print('This option is not available')
        if (do_in_menu == '1'):
            list_of_ships=level(list_of_ships)
            game_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)
        if (do_in_menu == '2'):
            legend()
def level (list_of_ships):
    repeat=1
    while repeat:
        cls()
        lvl=str(input('Chose type of game:'+'\n'+'\n'+'1.Short'+'\n'+'\n'+'2.Middle'+'\n'+'\n'+'3.Full'+'\n'))
        if lvl=='1':
            list_of_ships=[3, 2, 1]
            repeat=0
            return list_of_ships
        elif lvl=='2':
            list_of_ships=[4, 3, 2, 2, 1, 1]   
            repeat=0
            return list_of_ships
        elif lvl=='3':
            list_of_ships=[4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
            repeat=0
            return list_of_ships
        else:
            repeat=1    
cls()
menu(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)

