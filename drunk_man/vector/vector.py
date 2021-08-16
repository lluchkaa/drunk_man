from typing import Union, overload
from .vector_mode import VectorMode
from math import degrees, radians, sqrt, atan2, sin, cos


class Vector:
    def __init__(self, x: float = 0, y: float = 0, *, r: float = 0, a: float = 0, mode: VectorMode = VectorMode.xy) -> None:
        if mode == VectorMode.ra:
            self.x = r * cos(a)
            self.y = r * sin(a)
        else:
            self.x = x
            self.y = y

    @property
    def r(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    @r.setter
    def r(self, val: float):
        a = self.a
        self.x = val * cos(a)
        self.y = val * sin(a)

    @property
    def a(self):
        return atan2(self.y, self.x)

    @a.setter
    def a(self, val: float):
        r = self.r
        self.x = r * cos(val)
        self.y = r * sin(val)

    @property
    def deg(self):
        return degrees(self.a)

    @deg.setter
    def deg(self, val: float):
        self.a = radians(val)

    def __str__(self) -> str:
        return f'Vector({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'x = {self.x}, y = {self.y}'

    def __add__(self, vector: 'Vector'):
        return Vector(x=self.x+vector.x, y=self.y+vector.y)

    def __sub__(self, vector: 'Vector'):
        return Vector(x=self.x-vector.x, y=self.y-vector.y)

    @overload
    def __mul__(self, k: Union[float, int]) -> 'Vector': ...

    @overload
    def __mul__(self, vector: 'Vector') -> float: ...

    def __mul__(self, value: Union['Vector', float, int]) -> Union['Vector', float]:
        if isinstance(value, (int, float)):
            return Vector(x=self.x*value, y=self.y*value)
        elif isinstance(value, Vector):
            return self.x * value.x + self.y * value.y
        else:
            return None
