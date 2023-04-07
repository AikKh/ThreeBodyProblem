import pygame
from body import Body
from vector import Vector

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

class Slider:
    
    def __init__(self, pos: Vector, size: Vector, value, minimum, maximum):
        self.pos = pos
        self.size = size
        self.value = value
        self.minimum = minimum
        self.maximum = maximum

        self.knob_width = self.size.Y - 10
        self.knob_height = self.size.Y + 10
        self.bar_rect = pygame.Rect(*pos, *size)
        self.knob_rect = pygame.Rect(self.get_knob_x(), pos.Y - 5, self.knob_width, self.knob_height)
        self.font = pygame.font.Font(None, 36)
        self.dragging = False
        self.on_change = lambda value: None
        
    def get_knob_x(self):
        return self.pos.X + (self.value - self.minimum) / (self.maximum - self.minimum) * (self.size.X - self.knob_width) + (self.knob_width / 2)
    
    def set_values(self, on_change, min: int = None, max: int = None, value: int = None):
        self.minimum = min if min else self.minimum
        self.maximum = max if max else self.maximum
        self.on_change = on_change

        self.value = value if value else self.minimum
        self.knob_rect.centerx = self.get_knob_x()

    def update(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.knob_rect.collidepoint(event.pos):
                self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.knob_rect.centerx = self.get_knob_x()

                self.value = int(self.minimum + (event.pos[0] - self.pos.X) / self.size.X * (self.maximum - self.minimum))
                self.value = min(max(self.value, self.minimum), self.maximum)
                
                self.on_change(self.value)

        
    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.bar_rect)
        pygame.draw.rect(screen, WHITE, self.knob_rect)

        text = self.font.render(str(self.value if self.value < self.maximum else "Max"), True, WHITE)
        text_rect = text.get_rect(center=(self.knob_rect.centerx, self.knob_rect.centery + self.knob_height))
        screen.blit(text, text_rect)