import pygame
import sys
from pygame.locals import *
import random

pygame.init()
frame_rate = pygame.time.Clock()

# colour variables
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

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
            pygame.draw.rect(self.game.window, RED, [[self.x, self.y], [square_lat, square_lat]], 2)
        else:
            pygame.draw.rect(self.game.window, WHITE, [[self.x, self.y], [square_lat, square_lat]], 2)

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
    def __init__(self, game, x, y, selected = 0):
        super().__init__(game, x, y, selected)

    # NU APAR POZELE
    # TREBUIE INSERATA IMAGINEA ALTCUMVA

    def draw(self):
        line = pygame.image.load(r'C:\Users\Radu Ana Maria\Desktop\PipeGameW-main\line_pipe_1.png')
        self.window.blit(line,(x_start + square_lat, y_start))


class PipeCorner(square):
    def __init__(self, game, x, y, selected = 0):
        super().__init__(game, x, y, selected)

    def draw(self):
        corner = pygame.image.load(r'C:\Users\Radu Ana Maria\Desktop\PipeGameW-main\corner_pipe_1.png')
        self.window.blit(corner,(x_start,y_start))


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
                sq = square(self, x, y, pipe_type_initial[i][j])
                aux.append(sq)
                x += square_lat
            y += square_lat
            grid.append(aux)
        return grid


    def draw(self, grid):
        pygame.time.Clock().tick(60)
        pygame.display.update()

        # drawing the wallpaper
        wallpaper = pygame.image.load(r'C:\Users\Radu Ana Maria\Desktop\PipeGameW-main\Fundal.png')
        self.window.blit(wallpaper,(0,0))

        # drawing the outline of the grid
        pygame.draw.rect(self.window, WHITE, [[x_start, y_start], [grid_width, grid_height]], 2)

        # drawing the squares for the grid
        for line in grid:
            for sq in line:
                sq.draw()
        
        
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

    def selected(self, grid):
        for i in range (7):
            for j in range(10):
                if grid[i][j].isSelected():
                    return [i,j]

def main():
    gameInst = Game()
    gameInst.run()

main()