import math
import pygame
import vectors

class ray:
    def __init__(self, endpoint, direction):
        self.end = endpoint
        self.dir = direction

    def draw(self, surf):

        end = self.end + vectors.vecp(1000, self.dir).asCartesian()

        pygame.draw.line(surf, (255, 255, 255), self.end.astuple(), end.astuple())
