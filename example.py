#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------
SOKOBAN v1.0
Per Jonsson 2012-09-19
------------
"""

### MODULES
import os
import time


### FUNCTIONS
def play():
    """ Runs the main game sequence """

    level = False
    clear_screen()

    # Choose level
    while not level:
        try:
            level = input("\nWelcome to Sokoban, please choose da level (1-50)\n")
            int(level)
        except:
            print("\nPlease specify a number between 1-50!\n")
            level = False
        if (int(level) < 1 or int(level) > 50):
            print("\nPlease specify a number between 1-50!\n")
            level = False


    # Load user-picked level
    board = sokoban_load(int(level))
    sokoban_display(board)
    # Locate player in level and assign
    player = find_player(board)

    # Run the game - until player wins
    while True:
        # Let player make a move
        player = input_move_player(board, player)

        # If on a box, move both player and crate (if crate can move)
        if on_a_crate(board, player[1], player[2]) and player_can_move(board, player[1], player[2]):
            board = print_crate_move(board, player)
            board = print_player_move(board, player)

        # Else, move just player (if they can move)
        elif player_can_move(board, player[1], player[2]):
            board = print_player_move(board, player)

        # Else, reset and start over
        else:
            player = find_player(board)

        # Display board after each move
        sokoban_display(board)

        # Check if any unstored crates remain
        if did_player_win(board):
            print("\nCongratz! You completed level", level)
            print("\nNow exiting...")
            time.sleep(2)
            clear_screen()
            break
        # Else, start over
        else:
            continue
    #return

def did_player_win(board):
    """ Checks if any boxes remain in the board """
    for row in board:
        try:
            if row.index(items('crate')):
                return False
        except ValueError:
            pass
    return True

def items(item):
    """ Dictionary containg item characters """
    items = {'player': '@', 'crate': 'o', 'wall': '#', 'floor': ' ',
             'storage': '.', 'crate_stored': '*', 'player_stored': '+'}

    return items[item]


def clear_screen():
    """ Does what it says """
    os.system("clear")
    return

def sokoban_display(level=None, wall=None, player=None):
    """  """
    board=[]

    # First, make it clean
    clear_screen()

    #Print Sokoban user-picked level
    print_board(level)

    return

def input_move_player(board, player):
    """
    The player can move (l)eft, (r)ight, (u)p, (d)own, shove crates
    if empty spaces in front of them
    """
    direction = { 'l': -1, 'r': 1, 'u': -1, 'd': 1 }

    # Break if we get the correct input
    while True:
        move=input("\nMake your move (l)eft, (r)ight, (u)p, (d)own: ")
        try:
            if move in "'l''r''u''d'":
                if move in "lr":
                    player[1]+=direction[move]
                else:
                    player[2]+=direction[move]
                break
            else:
                print("\nWrong input!")
                continue
        except KeyError:
                print("\nWrong input!")
                continue
    return player


def find_player(board):
    """ Locate where the player (@) is in the board """
    x=0; y=0
    item='player'

    for row in board:
        try:
            if row.index(items('player')): #
                x=row.index(items('player'))
                y=board.index(row)
                item='player'
        except ValueError:
            pass

        try:
            if row.index(items('player_stored')):
                x=row.index(items('player_stored'))
                y=board.index(row)
                item='player_stored'
        except ValueError:
            pass

    return [item, x ,y]

def print_player_move(board, new_player):
    """ Prints the player's new position, restores the old one """
    # For reference
    old_player = find_player(board)

    # Replace old steps
    if old_player[0] == 'player_stored':
        board[old_player[2]][old_player[1]]=items('storage')
    else:
        board[old_player[2]][old_player[1]]=items('floor')

    # If on storage ground
    if board[new_player[2]][new_player[1]] == items('storage'):
        board[new_player[2]][new_player[1]]=items('player_stored')
    else:
        board[new_player[2]][new_player[1]]=items('player')

    return board

def player_can_move(board, to_x, to_y):
    """
    Returns True if it's possible to move a player to a new position, False if collision
    """
    can_move=False
    old_player = find_player(board)

    # If a crate is in the way
    if items('crate') in board[to_y][to_x] or items('crate_stored') in board[to_y][to_x]:
        # Look from where the player is coming from (their direction: pushing the box)
        x_move_crate = to_x - old_player[1]
        y_move_crate = to_y - old_player[2]
        # Can crate move?
        can_move = crate_can_move(board, to_x + x_move_crate, to_y + y_move_crate)

    # Nothing is in the way
    elif items('floor') in board[to_y][to_x] or items('storage') in board[to_y][to_x]:
        #print("\nplayer_can_move(): elif -> floor/storage = lugnt \n")
        can_move=True

    return can_move

def crate_can_move(board, to_x, to_y):
    """
    Returns True if the crate is free to move.
    """
    can_move=False

    try:
        if items('floor') in board[to_y][to_x] or items('storage') in board[to_y][to_x]:
            can_move=True
    except:
            print("\nSomething went wrong")

    return can_move

def on_a_crate(board, x, y):
    """ Check if the player will move to a crate's position """

    if items('crate') in board[y][x] or items('crate_stored') in board[y][x]:
        return True
    else:
        return False

def find_crate(board):
    """ Locates if a crate is left in the board, if not - the player won """
    x=0; y=0
    item='crate'

    for row in board:
        try:
            if row.index(items('crate')):
                x=row.index(items('crate'))
                y=board.index(row)
                item='crate'
        except ValueError:
            pass

        try:
            if row.index(items('crate_stored')):
                x=row.index(items('crate_stored'))
                y=board.index(row)
                item='crate_stored'
        except ValueError:
            pass

    return [item, x ,y]

def print_crate_move(board, crate):
    """ Print the crate's new position, erase the old one"""
    old_player = find_player(board)

    x_move_crate = crate[1] - old_player[1]
    y_move_crate = crate[2] - old_player[2]

    to_x = crate[1] + x_move_crate
    to_y = crate[2] + y_move_crate

    # If on a storage place or not
    print("\n Evaluerar board[crate[2]][crate[1]]", board[crate[2]][crate[1]])
    if board[crate[2]][crate[1]] == items('crate_stored'):
        board[crate[2]][crate[1]]=items('storage')
    else:
        board[crate[2]][crate[1]]=items('floor')

    # Change appearance of crate when stored
    if board[to_y][to_x] == items('storage'):
        board[to_y][to_x]=items('crate_stored')
    else:
        board[to_y][to_x]=items('crate')

    return board

def sokoban_load(level_input = 1):
    """
    Reads levels from a .txt file, converts into lists
    with rows for y-coordinates and columns for x-coordinates
    """
    board=[]
    row=[]
    input = open("sokoban_levels.txt", 'r')
    levels_file = input.readlines()
    level_no=1

    for line in levels_file:
        if level_no == level_input:
            for char in line:
                if char == '\n':
                    pass
                else:
                    row.append(char)
            board.append(row)
            row=[] # reset

        # If a blank line shows up we have come to the next level in the .txt
        if line == "\n":
            level_no+=1

    print("\nLoading level:", level_input, end='\n')
    time.sleep(2)

    return board

def print_board(board):
    """ Print level character by character, for each row print newline """

    for row in board:
        for char in row:
            print(char,end='')
        print()

    return board

############# RUN PROGRAM ###################

play()
