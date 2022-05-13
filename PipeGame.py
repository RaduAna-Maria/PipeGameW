# TO DO:
# functia de verificare pipe uri 
# celelalte poze
# animatie 

import pygame
import sys
import os
from pygame.locals import *
import random

pygame.init()
frame_rate = pygame.time.Clock()

# colour variables
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (81, 117, 161)
ORANGE = (241, 168, 42)

# window dimensions  
WIDTH =  1280
HEIGHT = 720

# grid global variables
square_lat = 80
x_start = 256
y_start = 72
grid_width = 10 * square_lat
grid_height = 7 * square_lat

# list of tuples for positions of tube pipes in the matrix
tube_list = [(0,1), (0,3), (0,4), (0,6), (0,8),
             (1,0), (1,4), (1,6), (1,7), (1,9),
             (2,1), (2,2), (2,3), (2,5), (2,7), (2,8),
             (3,0), (3,1), (3,4), (3,5), (3,6), (3,7), (3,9),
             (4,0), (4,2), (4,8), (4,9),
             (5,0), (5,1), (5,3), (5,5), (5,6), (5,7), (5,8), (5,9),
             (6,0), (6,4), (6,5), (6,6), (6,8)]

# codes for types of pipes and their orientation
# 0 = tube lef-right
# 1 = tube up-down
# 2 = corner up-right
# 3 = corner right-down
# 4 = corner down-left
# 5 = corner left-up
# DNK = a value that does not matter

# matrix for the maze at the start of the game
pipe_type_initial = []
for i in range(7):
    aux = []
    for j in range(10):
        if (i,j) in tube_list:
            aux.append(random.randrange(0,2,1))
        else:
            aux.append(random.randrange(2,6,1))
    pipe_type_initial.append(aux)

# list of tuples for positions of the correct way
# and the direction of the pipes
correct_way = [(0,0,4), (1,0,1), (2,0,2), (2,1,0), (2,2,0), (2,3,0), (2,4,4), 
               (3,4,1), (4,4,5), (4,3,3), (5,3,1), (6,3,2), (6,4,0), (6,5,0),
               (6,6,0), (6,7,5), (5,7,1), (4,7,4), (4,6,2), (3,6,1), (2,6,3),
               (2,7,0), (2,8,0), (2,9,4), (3,9,1), (4,9,1), (5,9,1), (6,9,2)]

class square: 
    def __init__(self, game, x, y, type, selected = 0):
        self.game = game
        self.x = x
        self.y = y
        self.s = selected
        self.type = type
    
    def draw(self):
        if self.isSelected():    
            pygame.draw.rect(self.game.window, ORANGE, [[self.x, self.y], [square_lat, square_lat]], 2)
        else:
            pygame.draw.rect(self.game.window, BLUE, [[self.x, self.y], [square_lat, square_lat]], 2)

        #PRESUPUN CA AICI AR TREBUI DESENATA SI POZA CU PIPE URI
        # if self.type == 0:
        #     tube = PipeTube(self.game, self.x, self.y, self.s)
        #     tube.draw()
        # else:
        #     pass

    def isSelected(self):
        return self.s

    def move(self, prev):
        self.s = 1
        prev.s = 0
        

class PipeTube(square):
    def __init__(self, game, x, y, direction, selected = 0):
        super().__init__(game, x, y, selected)
        self.direction = direction

    # NU APAR POZELE
    # TREBUIE INSERATA IMAGINEA ALTCUMVA

    def draw(self):
        tube = pygame.image.load(os.path.join('line_pipe_1.png'))
        tube = self.rotatePipe(tube) 
        self.game.window.blit(tube, (self.x, self.y))

    def rotatePipe(self, tube):
        if self.direction == 0:
            tube = pygame.transform.rotate(tube, 90)
        return tube

class PipeCorner(square):
    def __init__(self, game, x, y, direction, selected = 0):
        super().__init__(game, x, y, selected)
        self.direction = direction

    def draw(self):
        corner = pygame.image.load(os.path.join('corner_pipe_1.png'))
        corner = self.rotatePipe(corner)
        self.game.window.blit(corner, (self.x, self.y))
    
    def rotatePipe(self, corner):
        # if self.direction == 3:
        #     corner = pygame.transform.rotate(corner, 90)
        # elif self.direction == 4:
        #     corner = pygame.transform.rotate(corner, 180)
        # elif self.direction == 5:
        #     corner = pygame.transform.rotate(corner, 270)
        

        # if self.direction == 2 or self.direction == 3 or self.direction == 4:
        #         self.direction += 1
        # elif self.direction == 5:
        #         self.direction = 2
        d = 2       
        while d != self.direction: # 2 3 4 5 
            corner = pygame.transform.rotate(corner, -90)
            d += 1
            if d > 5:
                d = 2
        return corner


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('Pipe Game')
        
    def gridSquare(self):
        grid = []
        y = y_start
        for i in range(7):
            aux = []
            x = x_start
            for j in range(10):
                if (i, j) in tube_list:
                    sq = square(self, x, y, "tube")
                else:
                    sq = square(self, x, y, "corner")
                aux.append(sq)
                x += square_lat
            y += square_lat
            grid.append(aux)
        return grid


    def draw(self, grid):
        pygame.time.Clock().tick(60)
        pygame.display.update()

        # drawing the wallpaper
        wallpaper = pygame.image.load(os.path.join('Fundal.png'))
        self.window.blit(wallpaper,(0,0))

        # drawing the outline of the grid
        pygame.draw.rect(self.window, WHITE, [[x_start, y_start], [grid_width, grid_height]], 2)

        # drawing the squares for the grid
        i = 0
        for line in grid:
            j = 0
            for sq in line:                
                if sq.type == "tube":
                    pipe = PipeTube(self, sq.x, sq.y, pipe_type_initial[i][j])
                else:
                    pipe = PipeCorner(self, sq.x, sq.y, pipe_type_initial[i][j])
                pipe.draw()
                sq.draw()
                j += 1
            i += 1
        
        
        
    def run(self):
        grid = self.gridSquare()
        grid[0][0].s = 1 
        while True:
            self.draw(grid)    
            self.input(grid)        

    def input(self, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == KEYDOWN:
                [i,j] = self.selected(grid)
                if event.key == K_UP:
                    self.moveUp(grid, i, j)
                if event.key == K_DOWN:    
                    self.moveDown(grid, i, j)
                if event.key == K_RIGHT:
                    self.moveRight(grid, i, j)
                if event.key == K_LEFT:
                    self.moveLeft(grid, i, j)
                if event.key == K_SPACE:
                    self.rotate(grid, i, j)
    def moveUp(self, grid, i, j):
        if i == 0:
            grid[6][j].move(grid[i][j])
        else:
            grid[i-1][j].move(grid[i][j])

    def moveDown(self, grid, i, j):
        if i == 6:
            grid[0][j].move(grid[i][j])
        else:
            grid[i + 1][j].move(grid[i][j])

    def moveLeft(self, grid, i, j):
        if j == 0:
            grid[i][9].move(grid[i][j])
        else:
            grid[i][j - 1].move(grid[i][j])

    def moveRight(self, grid, i, j):
        if j == 9:
            grid[i][0].move(grid[i][j])
        else:
            grid[i][j + 1].move(grid[i][j])

    def rotate(self, grid, i, j):
        if grid[i][j].type == "tube":
            if pipe_type_initial[i][j] == 0:
                pipe_type_initial[i][j] = 1
            else:
                pipe_type_initial[i][j] = 0
            pipe = PipeTube(self, grid[i][j].x, grid[i][j].y, pipe_type_initial[i][j])
        else:
            if pipe_type_initial[i][j] == 2 or pipe_type_initial[i][j] == 3 or pipe_type_initial[i][j] == 4:
                pipe_type_initial[i][j] += 1
            elif pipe_type_initial[i][j] == 5:
                pipe_type_initial[i][j] = 2
            pipe = PipeCorner(self, grid[i][j].x, grid[i][j].y, pipe_type_initial[i][j])  
        pipe.draw()

        

    def selected(self, grid):
        for i in range (7):
            for j in range(10):
                if grid[i][j].isSelected():
                    return [i,j]

def main():
    gameInst = Game()
    gameInst.run()

main()