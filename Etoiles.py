import random
import pygame
import core
from pygame import Vector2


class Etoiles:

    def __init__(self):
        self.rayon = 10
        self.position = random.randint(0, 10000)
        self.tuple3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.nom = "étoiles"


for e in range(0, 100000):
    x = random.uniform(100, 300)
    y = random.uniform(100, 300)
