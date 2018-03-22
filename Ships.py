import os
import copy
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
base_matrix = [
    ['\ ', ' A ', ' B ', ' C ', ' D ', ' E ',' F ', ' G ', ' H ', ' I ', ' J '],
    ['1 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['2 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['3 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['4 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['5 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['6 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['7 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['8 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['9 ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ',' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ '],
    ['10', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ', ' ~ ']
    ]
player1_board = copy.deepcopy(base_matrix)
player2_board = copy.deepcopy(base_matrix)
player1_game = copy.deepcopy(base_matrix)
player2_game = copy.deepcopy(base_matrix)
list_of_ships = [1]
counter1 = 0
counter2 = 0


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
            if matrix[(lines + x)][(cols)] == ' 0 ':
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
            if matrix[lines][(cols + x)] == ' 0 ':
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
            matrix[lines][(cols + x)] = ' 0 '
    elif dir == 'col':
        for x in range(0, size):
            matrix[(lines + x)][(cols)] = ' 0 '


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


def ship(size,matrix):
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
        ship(elem, matrix)
        cls()
    return matrix


def doubleboard():
    print('            PLAYER 1' +
          '                                                            ' + 'PLAYER 2', '\n', '\n', '\n')
    for i in range(0, 11):
        print(
            ''.join(player1_game[i]) + '                                    ' + ''.join(player2_game[i]))


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
                    if player2_board[lines][cols] == ' 0 ':
                        player2_board[lines][cols] = ' X '
                        player1_game[lines][cols] = ' X '
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
                    elif player2_board[lines][cols] == ' ~ ':
                        player2_board[lines][cols] = ' * '
                        player1_game[lines][cols] = ' * '
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
                    if player1_board[lines][cols] == ' 0 ':
                        player1_board[lines][cols] = ' X '
                        player2_game[lines][cols] = ' X '
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
                    elif player1_board[lines][cols] == ' ~ ':
                        player1_board[lines][cols] = ' * '
                        player2_game[lines][cols] = ' * '
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


def game_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns):
    cls()
    player1_board = player_set(list_of_ships, player1_board, 1)
    player2_board = player_set(list_of_ships, player2_board, 2)
    winner = fight_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)
    print('The winner is: player ' + str(winner))
    end = input('Press enter to go to main menu')
    menu(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)


def legend():
    cls()
    print('~  symbol of water')
    print('O  element of ship')
    print('X  hit')
    print('*  miss')
    end = input('Press enter to go to main menu')
    menu()


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
            game_for_2(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)
        if (do_in_menu == '2'):
            legend()
           
cls()
menu(player1_board, player2_board, player1_game, player2_game, list_of_ships, columns)