import pygame
import random

kleur_voedsel = (255, 0, 0)
veld_grootte = 20

class Food:
    def __init__(self, breedte, hoogte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.plaats_voedsel()

    def plaats_voedsel(self):
        self.x = round(random.randrange(0, self.breedte - veld_grootte) / veld_grootte) * veld_grootte
        self.y = round(random.randrange(0, self.hoogte - veld_grootte) / veld_grootte) * veld_grootte

    def teken(self, venster):
        pygame.draw.rect(venster, kleur_voedsel, pygame.Rect(self.x, self.y, veld_grootte, veld_grootte))
