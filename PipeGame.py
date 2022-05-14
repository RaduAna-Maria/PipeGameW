# TO DO:
# functia de verificare pipe uri ✔
# celelalte poze ✔
# animatie 
# sa mearga corect prin corner pipe
# sunete ✔
# iconita de la joc schimbata ✔

import pygame
import sys
import os
from pygame.locals import *
import random

pygame.mixer.init()
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

    def isSelected(self):
        return self.s

    def move(self, prev):
        self.s = 1
        prev.s = 0
    
    def walkHorizontal(self, grid, start, stop):
        walk1 = pygame.image.load(os.path.join('Walk1.jpg'))
        walk1 = pygame.transform.scale(walk1, (30, 30))
        walk2 = pygame.image.load(os.path.join('Walk2.jpg'))
        walk2 = pygame.transform.scale(walk2, (30, 30))
        turn = 0
        for x in range (start, stop, 4): 
            if turn % 2 == 0: 
                self.game.draw(grid)
                self.game.window.blit(walk1, (x, self.y + square_lat / 2 - 15))
                pygame.display.update()
                pygame.time.delay(10)
            else:
                self.game.draw(grid)
                self.game.window.blit(walk2, (x, self.y + square_lat / 2 - 15))
                pygame.display.update()
                pygame.time.delay(10)
            turn += 1

    def walkVertical(self, grid, start, stop):
        walk1 = pygame.image.load(os.path.join('Walk1.jpg'))
        walk1 = pygame.transform.scale(walk1, (30, 30))
        walk2 = pygame.image.load(os.path.join('Walk2.jpg'))
        walk2 = pygame.transform.scale(walk2, (30, 30))
        turn = 0
        for y in range (start, stop, 4): 
            if turn % 2 == 0: 
                self.game.draw(grid)
                self.game.window.blit(walk1, (self.x + square_lat / 2 - 15, y))
                pygame.display.update()
                pygame.time.delay(10)
            else:
                self.game.draw(grid)
                self.game.window.blit(walk2, (self.x + square_lat / 2 - 15, y))
                pygame.display.update()
                pygame.time.delay(10)
            turn += 1
            

class PipeTube(square):
    def __init__(self, game, x, y, direction, selected = 0):
        super().__init__(game, x, y, selected)
        self.direction = direction

    def draw(self):
        tube = pygame.image.load(os.path.join('line_pipe_1.png'))
        tube = self.rotatePipe(tube) 
        self.game.window.blit(tube, (self.x, self.y))

    def rotatePipe(self, tube):
        if self.direction == 0:
            tube = pygame.transform.rotate(tube, 90)
        return tube
    
    def walk(self, grid):
        if self.direction == 0:
            self.walkHorizontal(grid, self.x, self.x + square_lat)
        else: 
            self.walkVertical(grid, self.y, self.y + square_lat)

class PipeCorner(square):
    def __init__(self, game, x, y, direction, selected = 0):
        super().__init__(game, x, y, selected)
        self.direction = direction

    def draw(self):
        corner = pygame.image.load(os.path.join('corner_pipe_1.png'))
        corner = self.rotatePipe(corner)
        self.game.window.blit(corner, (self.x, self.y))
    
    def rotatePipe(self, corner):
        d = 2       
        while d != self.direction: 
            corner = pygame.transform.rotate(corner, -90)
            d += 1
            if d > 5:
                d = 2
        return corner

    # e o problema si la square ul (5,7)
    # Nu merge corect
    def walk(self, grid):
        if self.direction == 2:
            self.walkVertical(grid, self.y, self.y + square_lat // 2)
            self.walkHorizontal(grid, self.x + square_lat // 2, self.x + square_lat)
        elif self.direction == 3:
            self.walkVertical(grid, self.y + square_lat, self.y + square_lat // 2)
            self.walkHorizontal(grid, self.x + square_lat // 2, self.x + square_lat)
        elif self.direction == 4:
            self.walkHorizontal(grid, self.x, self.x + square_lat // 2)
            self.walkVertical(grid, self.y + square_lat // 2, self.y + square_lat)
        else:
            self.walkHorizontal(grid, self.x, self.x + square_lat // 2)
            self.walkVertical(grid, self.y + square_lat // 2, self.y + square_lat)
            

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

        # drawing the squares and the pipes for the grid
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
        icon = pygame.image.load(os.path.join('Icon.png'))
        pygame.display.set_icon(icon)

        grid = self.gridSquare()
        grid[0][0].s = 1 
        solve = self.isSolved()
        
        while solve:
            self.draw(grid)    
            self.input(grid)  
            solve = self.isSolved()
        self.walk(grid)
        
            

    def input(self, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == KEYDOWN:
                [i,j] = self.selected(grid)
                if event.key == K_UP:
                    self.music('select_02', 0.5)
                    self.moveUp(grid, i, j)
                if event.key == K_DOWN:  
                    self.music('select_02', 0.5)
                    self.moveDown(grid, i, j)
                if event.key == K_RIGHT:
                    self.music('select_02', 0.5)
                    self.moveRight(grid, i, j)
                if event.key == K_LEFT:
                    self.music('select_02', 0.5)
                    self.moveLeft(grid, i, j)
                if event.key == K_SPACE:
                    self.music('selrot_01', 0.7)
                    self.rotate(grid, i, j)

    def music(self, sound, vol):
        pygame.mixer.music.load(os.path.join(sound))
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.play()

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

    def isSolved(self):
        for (i, j, d) in correct_way:
            if pipe_type_initial[i][j] != d:
                return True
        return False 

    def selected(self, grid):
        for i in range (7):
            for j in range(10):
                if grid[i][j].isSelected():
                    return [i,j]
    
    def walk(self, grid):
        for (i, j, d) in correct_way:
            if d == 0 or d == 1:
                pipe = PipeTube(self, grid[i][j].x, grid[i][j].y, d)
            else:
                pipe = PipeCorner(self, grid[i][j].x, grid[i][j].y, d)
            pipe.walk(grid)
            

def main():
    gameInst = Game()
    gameInst.run()

main()