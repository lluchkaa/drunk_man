from vector import Vector, VectorMode
from math import pi
import random


class DrunkMan:
    def __init__(self, *, step: float = 1, direction: float = 0, promile: int = 0) -> None:
        self.position = Vector(x=0, y=0)
        self.step = step
        self.direction = direction

        assert 0 <= promile <= 1, 'Promile must be in range [0, 1]'
        self.promile = promile

    def __update_direction(self):
        ang = self.promile * pi
        self.direction += random.uniform(-ang, ang)
        return self.direction

    def go(self):
        self.__update_direction()
        self.position += Vector(mode=VectorMode.ra,
                                r=self.step, a=self.direction)
