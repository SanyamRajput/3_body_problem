
import tkinter as tk
import vector as v

G = 1  # Gravitational constant


class CelestialBody:
    def __init__(self, x, y, vx, vy, mass, color, radius):
        self.pos = v.Vector(x, y)
        self.vel = v.Vector(vx, vy)
        self.mass = mass
        self.color = color
        self.radius = radius

    def acceleration(self, other):
        r_vec = other.pos - self.pos
        r_mag = r_vec.magnitude()
        if r_mag == 0:
            return v.Vector(0, 0)  # Avoid division by zero
        force_mag = G * other.mass / (r_mag ** 2)
        return r_vec.unit() * force_mag
    
    def update(self, acceleration, dt):
        self.vel = self.vel + (acceleration * dt)
        self.pos = self.pos + (self.vel * dt)


