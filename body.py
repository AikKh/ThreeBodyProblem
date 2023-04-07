from vector import Vector
from random import randrange as rd


class Body:

    def __init__(self, pos: Vector, direction: Vector, mass: float, color: tuple[int, int, int] = (0, 0, 0), radius = 0) -> None:
        self._pos: Vector = pos
        self._dir: Vector = direction
        self._mass: float = mass
        self._radius: float = (mass ** (1/3)) if not radius else radius
        self._color: tuple[int, int, int] = color if sum(color) > 0 else (rd(255), rd(255), rd(255))
        self._path = [] 

    def set_mass(self, mass):
        self._mass: float = mass
        self._radius: float = (mass ** (1/3))

    def move(self):
        if len(self._path) > 800:
            del self._path[0]
        self._path.append(tuple(self._pos))
        self._pos += self._dir

    