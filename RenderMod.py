#Renderer

#IMPORTATIONS

import pygame
import pygame.gfxdraw
from pygame.locals import *
#import pygame.freetype

import AlgoMod

#Classes

class Renderer:
    def __init__(self, projSettings):
        
        pygame.init()
        pygame.font.init()

        self.largeur = projSettings["height"]
        self.longueur = projSettings["width"]
        self.couleurFenetre = (30, 30, 30)

        self.fenetre = pygame.display.set_mode((self.longueur, (self.largeur)))
        self.fonte = pygame.font.SysFont("arial", 30)
        self.FPSFont = pygame.font.SysFont("arial", 30)

    def Init(self):
        
        pygame.display.set_caption("3dEngine")
        self.fenetre.fill(self.couleurFenetre)
        pygame.display.flip()

    def Clear(self):
        
        self.fenetre.fill(self.couleurFenetre)

    def DrawTri(self, point1, point2, point3, luminance):

        #print("lum " + str(luminance))
        lum = abs(int(luminance * 255))
        color = (lum, lum, lum)
        #color = (lum, lum, lum)
        #print(color)
        #print("newRendered")
        #print(AlgoMod.ZVal([point1, point2, point3]))

        #print(point1)

        pygame.gfxdraw.filled_polygon(self.fenetre, [(point1[0], point1[1]),(point2[0], point2[1]),(point3[0], point3[1])], color)

        

        #pygame.draw.aaline(self.fenetre, (0,255,0), (point1[0], point1[1]), (point2[0], point2[1]))
        #pygame.draw.aaline(self.fenetre, (0,255,0), (point2[0], point2[1]), (point3[0], point3[1]))
        #pygame.draw.aaline(self.fenetre, (0,255,0), (point3[0], point3[1]), (point1[0], point1[1]))

        #print(point1[0], point1[1], point2[0], point2[1])
    
    def Show(self, deltaTime):

        #FPS COUNTER
        FPSRect = pygame.Rect(0, 0, 135, 35)
        pygame.draw.rect(self.fenetre, (0, 0, 0, 125), FPSRect, width=0)
        FPSText = "FPS : " + str(deltaTime)
        FPSSurface = self.FPSFont.render(FPSText, True, (255, 255, 0, 0))
        self.fenetre.blit(FPSSurface, (0,0))

        #pygame.draw.line(self.fenetre, (0,255,0), (0,0), (1400, 700))
        pygame.display.flip()
        #print("we done")
