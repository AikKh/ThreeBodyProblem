import pygame, sys
from vector import Vector 
from body import Body
from UI.slider import Slider
from UI.button import Button

class Screen:
    
    width, height = 1200, 700 
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Three-body problem in python")
    
    clock = pygame.time.Clock()
    fps = 60
    
    def __init__(self, object):
        self._object = object
        self._slider = Slider(Vector(50, 620), Vector(400, 40), 0, 0, 1000)

        self._buttons = []

        i = 0
        for i, body in enumerate(self._object._bodies):
            func = lambda body=body: self._slider.set_values(on_change = lambda value: body.set_mass(value), 
                                                             min = 10, 
                                                             max = 1000, 
                                                             value = body._mass)
            
            self._buttons.append(Button(50 + i * 50, 50, 20, body._color, func = func))

        manage_speed = lambda: self._slider.set_values(on_change = lambda value: self._object.set_speed(value), 
                                                        min = 1, 
                                                        max = self._object.MaxSpeed, 
                                                        value = self._object._speed)

        self._buttons.append(Button(50 + (i + 1) * 50, 50, 20, (255, 255, 255), manage_speed, width=10))
            
        super().__init__()


    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            self._object.draw(self.screen)
            self._slider.draw(self.screen)
            for button in self._buttons:
                button.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)
            
            for event in pygame.event.get():
                self._slider.update(event)
                for button in self._buttons:
                    button.update(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
