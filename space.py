import pygame, sys
from math import sqrt
from time import sleep
from body import Body
from vector import Vector
from threading import Thread


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

pygame.init()

class Space(Thread):

    G: float = 6.674 * 10 ** -1
    MaxSpeed: int = 1000 

    def __init__(self, *bodies: Body, speed: float = 0) -> None:
        self._bodies = bodies
        self._speed = speed
        super().__init__()

    def set_speed(self, value: int):
        self._speed = value

    @staticmethod
    def acceleration(body: Body, other: Body) -> Vector:
        distance = sqrt((other._pos.X - body._pos.X) ** 2 + (other._pos.Y - body._pos.Y) ** 2)
        return ((other._pos - body._pos) * other._mass * Space.G) / (distance ** 3)

    def step(self):
        for body in self._bodies:
            body.move()
        
        for body in self._bodies:
            others = (other for other in self._bodies if other is not body)

            result = body._dir
            for other in others:
                result += Space.acceleration(body, other) 

            body._dir = result

    def run(self) -> None:
        while True:
            sleep((Space.MaxSpeed - self._speed) / Space.MaxSpeed / 100)
            self.step()

    def draw(self, screen: pygame.Surface):
        for body in self._bodies:
            pygame.draw.circle(screen, body._color, tuple(body._pos), body._radius) # type: ignore
            lenght = len(body._path)
            for i in range(lenght - 1):
                color = (body._color[0] / lenght * i, body._color[1] / lenght * i, body._color[2] / lenght * i)
                pygame.draw.line(screen, color, body._path[i], body._path[i + 1]) # type: ignore