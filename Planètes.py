import pygame
import core
from pygame import Vector2
import random

class Planètes :

    def __init__(self):
        self.int = random.randint(50, 600)
        self.position = Vector2(random.randint(0, 1000), random.randint(0, 750))
        self.tuple3 = (255, 10, 0)
        self.nom = "planètes"


    core.main(setup, run)