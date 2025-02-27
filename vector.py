import math
import tkinter as tk

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def unit(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag) if mag != 0 else Vector(0, 0)
    
    def tuple(self):
        return self.x, self.y