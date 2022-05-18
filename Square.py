import pygame
import os
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
image_width = 50
image_height = 70



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
    
    def walkRight(self, grid, start, stop, y):
        walk2 = pygame.image.load(os.path.join('Walk', 'Vener_walk_right2.png'))
        walk3 = pygame.image.load(os.path.join('Walk', 'Vener_walk_right3.png'))
        walk1 = pygame.image.load(os.path.join('Walk', 'Vener_walk_right1.png'))
        turn = 0
        for x in range (start, stop, 4): 
            if turn % 3 == 0: 
                self.game.draw(grid)
                self.game.window.blit(walk1, (x, y))
                pygame.display.update() 
            elif turn % 3 == 1:
                self.game.draw(grid)
                self.game.window.blit(walk2, (x, self.y + square_lat / 2  - image_height))
                pygame.display.update() 
            else:
                self.game.draw(grid)
                self.game.window.blit(walk3, (x, self.y + square_lat / 2  - image_height))
                pygame.display.update() 
            turn += 1
    
    def walkLeft(self, grid, start, stop, y):
        walk2 = pygame.image.load(os.path.join('Walk', 'Vener_walk_left2.png'))
        walk3 = pygame.image.load(os.path.join('Walk', 'Vener_walk_left3.png'))
        walk1 = pygame.image.load(os.path.join('Walk', 'Vener_walk_left1.png'))
        turn = 0
        for x in range (start, stop, -4): 
            if turn % 3 == 0: 
                self.game.draw(grid)
                self.game.window.blit(walk1, (x, y))
                pygame.display.update() 
            elif turn % 3 == 1:
                self.game.draw(grid)
                self.game.window.blit(walk2, (x, y))
                pygame.display.update() 
            else:
                self.game.draw(grid)
                self.game.window.blit(walk3, (x, y))
                pygame.display.update() 
            turn += 1

    def walkUp(self, grid, start, stop, x):
        walk1 = pygame.image.load(os.path.join('Walk', 'Vener_walk_up1.png'))
        walk2 = pygame.image.load(os.path.join('Walk', 'Vener_walk_up2.png'))
        walk3 = pygame.image.load(os.path.join('Walk', 'Vener_walk_up3.png'))
        turn = 0
        for y in range (start, stop, -4): 
            if turn % 3 == 0: 
                self.game.draw(grid)
                self.game.window.blit(walk1, (x, y))
                pygame.display.update() 
            elif turn % 3 == 1:
                self.game.draw(grid)
                self.game.window.blit(walk2, (x, y ))
                pygame.display.update() 
            else:
                self.game.draw(grid)
                self.game.window.blit(walk3, (x, y ))
                pygame.display.update() 
            turn += 1
            
    def walkDown(self, grid, start, stop, x):
        walk1 = pygame.image.load(os.path.join('Walk', 'Vener_walk_down1.png'))
        walk2 = pygame.image.load(os.path.join('Walk', 'Vener_walk_down2.png'))
        walk3 = pygame.image.load(os.path.join('Walk', 'Vener_walk_down3.png'))
        turn = 0
        for y in range(start, stop, 4): 
            if turn % 3 == 0: 
                self.game.draw(grid)
                self.game.window.blit(walk1, (x, y))
                pygame.display.update() 
            elif turn % 3 == 1:
                self.game.draw(grid)
                self.game.window.blit(walk2, (x, y))
                pygame.display.update() 
            else:
                self.game.draw(grid)
                self.game.window.blit(walk3, (x, y))
                pygame.display.update() 
            turn += 1
