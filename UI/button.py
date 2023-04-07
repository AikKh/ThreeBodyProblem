import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Button:

    def __init__(self, x, y, radius, color, func, width = 0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.button_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.func = func
        self.width = width
        
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)
    
    def update(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(pos):
                self.func()
