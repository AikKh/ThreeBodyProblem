from random import randrange as rd
from system import System, Space, Body, Vector


class Random(System):

    def __init__(self) -> None:
        sun = Body(Vector(400, 350), Vector(0, 0), 100_000, (255, 216, 0))
        space = Space(*(Body(Vector(rd(600, 1200), rd(0, 700)), 
                        Vector(0, -15),
                        rd(1000, 8000) / 500)
                        for _ in range(rd(10, 12))),
                        sun, 
                        speed=100)
        super().__init__(space)
