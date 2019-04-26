import pygame
from pygame.locals import *
import AI


def judge(x, y, status, cb):
    count1, count2, count3, count4 = 0, 0, 0, 0
    i = x - 1
    while i >= 0:
        if cb[i][y] == status:
            count1 += 1
            i -= 1
        else:
            break
    i = x + 1
    while i < 15:
        if cb[i][y] == status:
            count1 += 1
            i += 1
        else:
            break

    j = y - 1
    while j >= 0:
        if cb[x][j] == status:
            count2 += 1
            j -= 1
        else:
            break
    j = y + 1
    while j < 15:
        if cb[x][j] == status:
            count2 += 1
            j += 1
        else:
            break

    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        if cb[i][j] == status:
            count3 += 1
            i -= 1
            j -= 1
        else:
            break
    i, j = x + 1, y + 1
    while i < 15 and j < 15:
        if cb[i][j] == status:
            count3 += 1
            i += 1
            j += 1
        else:
            break

    i, j = x + 1, y - 1
    while i < 15 and j >= 0:
        if cb[i][j] == status:
            count4 += 1
            i += 1
            j -= 1
        else:
            break
    i, j = x - 1, y + 1
    while i > 0 and j < 15:
        if cb[i][j] == status:
            count4 += 1
            i -= 1
            j += 1
        else:
            break

    if count1 >= 4 or count2 >= 4 or count3 >= 4 or count4 >= 4:
        print("WIN")
        return True
    else:
        print(count1, count2, count3, count4, x, y, status, cb[x][y])
        return False


class Chess(object):
    def __init__(self):
        self.cb = [[0 for i in range(15)] for j in range(15)]

    def fall(self, x, y, status):
        if x < 0 or x > 14 or y < 0 or y > 14:
            return None
        self.cb[x][y] = status
        print("fall done")

    def isEmpty(self, m, n):
        if self.cb[m][n] != 0:
            return False
        else:
            return True

def mode1():
    pygame.init()
    bg = 'bg3.png'
    white_chess = 'white1.png'
    black_chess = 'black1.png'

    screen = pygame.display.set_mode((750, 750), 0, 32)
    background = pygame.image.load(bg).convert()
    white = pygame.image.load(white_chess).convert_alpha()
    black = pygame.image.load(black_chess).convert_alpha()

    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("times", 45)
    pygame.display.set_caption('Gomoku')

    pygame.event.set_allowed([MOUSEBUTTONDOWN, MOUSEBUTTONUP])

    dot_list = [(25 + i * 50 - white.get_width() / 2, 25 + j * 50 - white.get_height() / 2)
                for i in range(15) for j in range(15)]

    chess = Chess()
    status = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if 25 <= x <= 725 and 25 <= y <= 725 and ((x - 25) % 50 <= 15 or (x - 25) % 50 >= 0) and (
                        (y - 25) % 50 <= 15 or (y - 25) % 50 >= 0):
                    m = int(round((x-25)/50))
                    n = int(round((y-25)/50))
                    if not chess.isEmpty(m, n):
                        continue
                    chess.fall(m, n, status)
                    if status == 1: screen.blit(black, dot_list[15 * m + n])
                    if status == -1: screen.blit(white, dot_list[15 * m + n])
                    if judge(m, n, 1, chess.cb):
                        screen.blit(font.render('GAME OVER, BLACK WINS', True, (255, 0, 0)), (100, 350))
                    if judge(m, n, -1, chess.cb):
                        screen.blit(font.render('GAME OVER, WHITE WINS', True, (255, 0, 0)), (100, 350))
                    status = (-1)*status

        pygame.display.update()


def mode2():
    pygame.init()
    bg = 'bg3.png'
    white_chess = 'white1.png'
    black_chess = 'black1.png'

    screen = pygame.display.set_mode((750, 750), 0, 32)
    background = pygame.image.load(bg).convert()
    white = pygame.image.load(white_chess).convert_alpha()
    black = pygame.image.load(black_chess).convert_alpha()

    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("times", 45)
    pygame.display.set_caption('Gomoku')

    pygame.event.set_allowed([MOUSEBUTTONDOWN, MOUSEBUTTONUP])

    dot_list = [(25 + i * 50 - white.get_width() / 2, 25 + j * 50 - white.get_height() / 2)
                for i in range(15) for j in range(15)]

    chess = Chess()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if 25 <= x <= 725 and 25 <= y <= 725 and ((x - 25) % 50 <= 15 or (x - 25) % 50 >= 0) and (
                        (y - 25) % 50 <= 15 or (y - 25) % 50 >= 0):
                    m = int(round((x - 25) / 50))
                    n = int(round((y - 25) / 50))
                    if not chess.isEmpty(m, n):
                        continue
                    chess.fall(m, n, 1)
                    screen.blit(black, dot_list[15 * m + n])
                    if judge(m, n, 1, chess.cb):
                        screen.blit(font.render('GAME OVER, BLACK WINS', True, (255, 0, 0)), (100, 350))

                    i, j = AI.AIgo(chess.cb)
                    print(i, j)
                    chess.fall(i, j, -1)
                    screen.blit(white, dot_list[15 * i + j])
                    if judge(i, j, -1, chess.cb):
                        screen.blit(font.render('GAME OVER, WHITE WINS', True, (255, 0, 0)), (100, 350))

        pygame.display.update()


M = input("Please choose mode:")
if M == "1":
    mode1()
elif M == "2":
    mode2()
else:
    print("Wrong mode")


