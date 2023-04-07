# from random import randrange as rd
from system import System, Space, Body, Vector


class FigureEight(System):

    def __init__(self) -> None:
        mass = 600
        center = Vector(600, 350)
        vigure8Position = Vector(0.97000436, -0.24308753) * 400
        vigure8Velocity = Vector(-0.93240737, -0.86473146) 

        bod1 = Body(center, vigure8Velocity, mass)
        bod2 = Body(vigure8Position + center, Vector(-vigure8Velocity.X / 2, -vigure8Velocity.Y / 2), mass)
        bod3 = Body(Vector(-vigure8Position.X, -vigure8Position.Y) + center, Vector(-vigure8Velocity.X / 2, -vigure8Velocity.Y / 2), mass)

        space = space = Space(bod1, bod2, bod3, speed=10)
        super().__init__(space)