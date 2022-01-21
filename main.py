import pygame, sys
import TicMod as tictactoe
import numpy as np
import time

board = np.zeros((3, 3), dtype=int)
HUMAN = -1
AI = +1
width = 600
height = 600
screen = pygame.display.set_mode((width, height))


def message(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [600/2, 600/2])


def check_space(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def found_winner(board, player):
    empty_box = len(tictactoe.empty_place(board))
    if empty_box == 0:
        print("Draw")
        message("Tie", (0, 0, 0))
        pygame.display.update()
        time.sleep(2)
        sys.exit()

    elif tictactoe.check_winner(board, player):
        message("You Win", (200, 0, 75))
        pygame.display.update()
        time.sleep(2)
        sys.exit()

    elif tictactoe.check_winner(board, -player):

        message("You Lost", (200, 0, 75))
        pygame.display.update()
        time.sleep(2)
        sys.exit()

def ai_move():
    row, col = tictactoe.play_game(board)
    board[int(row)][int(col)] = 1
    pygame.draw.line(screen, (100, 100, 100), (int(col*200+20), int(row*200+20))
                     , (int(col*200+175),int(row*200+175)), 10)
    pygame.draw.line(screen, (100, 100, 100), (int(col * 200 + 175), int(row * 200 + 20))
                     , (int(col * 200 + 20), int(row * 200 + 175)), 10)
    found_winner(board, HUMAN)


def line_draw():
    screen_color = (144, 238, 144)
    global screen
    line_color = (255, 255, 255)
    pygame.display.set_caption("TIC-TAC-TOE")
    screen.fill(screen_color)
    pygame.draw.line(screen, line_color, (10, 200), (590, 200), 10)
    pygame.draw.line(screen, line_color, (10, 400), (590, 400), 10)
    pygame.draw.line(screen, line_color, (200, 10), (200, 590), 10)
    pygame.draw.line(screen, line_color, (400, 10), (400, 590), 10)


pygame.init()
line_draw()

font = pygame.font.SysFont('arial', 33)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // 200
            row = event.pos[1] // 200
            if check_space(row, col):
                board[row][col] = HUMAN
                pygame.draw.circle(screen, (220, 100, 90),(int(col*200+100),int(row *200+100)), 80, 10)
                found_winner(board, HUMAN)
                ai_move()
    pygame.display.update()
