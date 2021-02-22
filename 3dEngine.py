#3d engine

#IMPORTATIONS

import pygame

import EngineMod

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

for frameCount in range(frames):
    engine.Update()

    clock.tick(fps)


