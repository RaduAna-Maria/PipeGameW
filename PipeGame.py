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


class square: 
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(self.game.window, RED, [[self.x, self.y], [square_lat, square_lat]], 2)

    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def moveUp(self):
        if self.y - square_lat < y_start:
            self.setPosition(self.x, grid_height)
            self.draw()
        else:
            self.setPosition(self, self.x, self.y - square_lat)
            self.draw()
        
    def moveDown(self):
        pass
    def moveRight(self):
        pass
    def moveLeft(self):
        pass

class PipeTube(square):
    def __init__(self):
        super().__init__()

class PipeCorner(square):
    def __init__(self):
        super().__init__()

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('Pipe Game')
        
    def draw(self):
        pygame.time.Clock().tick(60)
        pygame.display.update()

        # drawing the outline of the grid
        pygame.draw.rect(self.window, WHITE, [[x_start, y_start], [grid_width, grid_height]], 2)

        # drawing the horizontal lines of the grid
        x = x_start + grid_width
        y = y_start + square_lat
        for i in range(7):
            pygame.draw.line(self.window, WHITE, [x_start, y], [x, y])
            y += square_lat

        # drawing the vertical lines of the grid
        x = x_start + square_lat
        y = y_start + grid_height
        for i in range(10):
            pygame.draw.line(self.window, WHITE, [x, y_start], [x, y])
            x += 80
        
       
        

    def run(self):
        while True:
            self.input()
            # self.update()
            self.draw()
    
    # def update(self):
        

    def input(self):
        # drawing the initial square
        sq = square(self, x_start, y_start)
        square.draw(sq)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    sq.moveUp()
        
            


def main():
    gameInst = Game()
    gameInst.run()


main()
