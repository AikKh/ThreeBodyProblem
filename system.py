from body import Body
from space import Space
from vector import Vector 
from screen import Screen
from abc import ABC, abstractmethod


class System(ABC):

    @abstractmethod
    def __init__(self, space: Space) -> None:
        self._space = space
        self._screen = Screen(space)

    def start(self):
        self._space.start()
        self._screen.run()
        self._space.join()
