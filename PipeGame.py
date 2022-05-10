import pygame as py

py.init()
frame_rate = py.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 600
HEIGHT = 400


class square: 
    def __init__(self):
        pass

class PipeTube(square):
    def __init__(self):
        super().__init__()

class PipeCorner(square):
    def __init__(self):
        super().__init__()

class Game:
    def __init__(self):
        self.window = py.display.set_mode((WIDTH, HEIGHT), 0, 32)
        py.display.set_caption('Pipe Game')
        
        