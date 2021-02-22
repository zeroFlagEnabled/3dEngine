#3d engine

#IMPORTATIONS

import pygame
from time import perf_counter
import EngineMod
import timeit

#CONSTANTES

height = 700
width = 1400

aspectRatio = height/width
fov = 90
zFar = 1000
zNear = 0.1

projSettings = {"height": height, "width": width, "aspectRatio": aspectRatio, "fov": fov, "zFar": zFar, "zNear": zNear}

fps = 60
lifeTime = 10
frames = fps * lifeTime

#INITIALISATION MOTEUR

engine = EngineMod.Engine(projSettings)
engine.Init()

clock = pygame.time.Clock()

#BOUCLE PRINCIPALE

FPSTimes = [0, 1]
deltaTime = [0,0,0,0]

for frameCount in range(frames):
    
    FPSTimes.append(perf_counter())
    #print(t2 - t1)

    deltaTime.append(int(1.0 / (FPSTimes[-1] - FPSTimes[-2])))
    stableDTime = int((deltaTime[-1] + deltaTime[-2] + deltaTime[-3] + deltaTime[-4] + deltaTime[-5]) / 5)
    #print("deltaTime = ", deltaTime[-1]) 
     
    engine.Update(stableDTime)

    clock.tick(fps)
    #t2 = perf_counter()


