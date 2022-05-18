from Square import *

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
    
    def walk(self, grid, dir):
        if self.direction == 0 and dir == "right":
            self.walkRight(grid, self.x, self.x + square_lat, self.y + square_lat / 2 - image_height )
            
        elif self.direction == 0 and dir == "left":
            self.walkLeft(grid, self.x + square_lat, self.x, self.y + square_lat / 2  - image_height)
        elif self.direction == 1 and dir == "up": 
            self.walkUp(grid, self.y + square_lat, self.y, self.x + square_lat / 2  - image_width // 2)
        else: 
            self.walkDown(grid, self.y, self.y + square_lat, self.x + square_lat / 2  - image_width // 2)

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

    def walk(self, grid, dir):
        if dir == "up":
            if self.direction == 2:
                self.walkLeft(grid, self.x + square_lat, self.x + square_lat // 2, self.y - 30)
                self.walkUp(grid, self.y + square_lat // 2, self.y, self.x + square_lat // 2)
            elif self.direction == 3:
                    self.walkUp(grid, self.y + square_lat, self.y + square_lat // 2, self.x + square_lat / 2  - image_width // 2)
                    self.walkRight(grid, self.x + square_lat // 2, self.x + square_lat, self.y + square_lat / 2  - image_height) 
            elif self.direction == 4:
                self.walkUp(grid, self.y + square_lat, self.y + square_lat // 2, self.x + square_lat / 2  - image_width // 2)
                self.walkLeft(grid, self.x + square_lat // 2, self.x, self.y + square_lat / 2  - image_height) 
            else:
                self.walkRight(grid, self.x, self.x + square_lat // 2, self.y + square_lat / 2  - image_height)
                self.walkUp(grid, self.y + square_lat // 2, self.y, self.x + square_lat / 2  - image_width // 2)
        else:
            if self.direction == 2:
                self.walkDown(grid, self.y, self.y + square_lat // 2, self.x + square_lat / 2  - image_width // 2)
                self.walkRight(grid, self.x + square_lat // 2, self.x + square_lat, self.y + square_lat / 2  - image_height)
            elif self.direction == 3:
                    self.walkLeft(grid, self.x + square_lat, self.x + square_lat // 2, self.y + square_lat / 2  - image_height)
                    self.walkDown(grid, self.y + square_lat // 2, self.y + square_lat, self.x + square_lat / 2  - image_width // 2)
            elif self.direction == 4:
                self.walkRight(grid, self.x, self.x + square_lat // 2, self.y + square_lat / 2  - image_height)
                self.walkDown(grid, self.y + square_lat // 2, self.y + square_lat, self.x + square_lat / 2  - image_width // 2)
            else:
                self.walkDown(grid, self.y, self.y + square_lat // 2, self.x + square_lat / 2  - image_width // 2)
                self.walkLeft(grid, self.x + square_lat // 2, self.x, self.y + square_lat / 2  - image_height)