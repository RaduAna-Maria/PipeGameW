import pygame
import sys
from pygame.locals import *

pygame.init()
frame_rate = pygame.time.Clock()

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

#types of pipes
# 0 = corner
# 1 = tube
pipe_type = [[0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
             [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
             [1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1, 1, 1, 0, 1, 0]]

tube_directions = {0: "up-down", 1:"left-right"}
corner_directions = {0: "up-right", 1:"right-down", 2:"down-left", 3:"left-up"}

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

    def isSelected(self):
        return self.s

    def move(self, prev):
        self.s = 1
        prev.s = 0
        

class PipeTube(square):
    def __init__(self, game, x, y, direction, selected = 0):
        super().__init__(game, x, y, selected)
        self.direction = direction

    def draw(self):
        tube = pygame.image.load('C:\Users\ana_m\Desktop\PipeGameW\Tube.png')
        return tube

class PipeCorner(square):
    def __init__(self, game, x, y, direction, selected = 0):
        super().__init__(game, x, y, selected)
        self.direction = direction


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
                sq = square(self, x, y)
                aux.append(sq)
                x += square_lat
            y += square_lat
            grid.append(aux)
        return grid


    def draw(self, grid):
        pygame.time.Clock().tick(60)
        pygame.display.update()

        # drawing the outline of the grid
        pygame.draw.rect(self.window, WHITE, [[x_start, y_start], [grid_width, grid_height]], 2)

        # drawing the lines of the grid
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