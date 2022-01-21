import numpy as np
from math import inf as Infinity
import math
import random

def empty_place(board):
    empty_states=[]
    for x,row in enumerate(board):
        for y,box in enumerate(row):
            if box == 0:
                axis = [x,y]
                empty_states.append(axis)
    return empty_states

def game_over(board):
    return check_winner(board,1) or check_winner(board,-1)

def give_value(board):
    if check_winner(board,1):
        return 1
    elif check_winner(board,-1):
       return -1
    else:
        return 0

def check_winner(board,value):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [value,value,value] in win_states:
        return True
    else:
        return False

count=0

def minimax(board, depth, turn):
    if turn == True:
        best_move = [-1,-1,-Infinity]
        value = +1
    else:
        best_move = [-1,-1,+Infinity]
        value = -1

    if depth == 0 or game_over(board):
        score = give_value(board)
        return [-1,-1,score]

    elif turn == True:
        empty = empty_place(board)
        for i in empty:
            row = i[0]
            col = i[1]
            board[row][col] = value
            score = minimax(board, depth-1, False)
            board[row][col] = 0
            if score[2]>best_move[2]:
                score[0],score[1] = row, col
                best_move = score

    elif turn == False:
        empty = empty_place(board)
        for i in empty:
            row = i[0]
            col = i[1]
            board[row][col] = value
            score = minimax(board, depth-1, True)
            board[row][col] = 0
            if score[2]<best_move[2]:
                score[0],score[1] = row, col
                best_move = score
    return best_move

def play_game(board):
    Turn = True
    depth = len(empty_place(board))
    score = minimax(board, depth, Turn)
    return score[0], score[1]
