import pygame
import random
from cube import Cube
from snake import Snake

width = 500
height = 500
rows = 20

global s, snack, win
s = Snake((255, 0, 0), (10, 10))
win = pygame.display.set_mode((width, height))

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (225, 225, 225), (x, 0), (x, w))
        pygame.draw.line(surface, (225, 225, 225), (0, y), (w, y)) 

def redrawWindow(snack):
    win.fill((0, 0, 0))
    drawGrid(width, rows, win)
    s.draw(win)
    snack.draw(win)
    pygame.display.update()
    pass

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1, rows - 1)
        y = random.randrange(1, rows - 1)

        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)

def main():
    snack = Cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        s.move()
        headPos = s.head.pos
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
            print("Score: ", len(s.body))
            s.reset((10, 10))
        
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = Cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print("Score: ", len(s.body))
                s.reset((10, 10))
                break
        
        redrawWindow(snack)

main()