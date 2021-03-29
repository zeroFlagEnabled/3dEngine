#Engine module

#IMPORTATIONS

import RenderMod
import SceneMod
import MatrixMod
import pygame

#Classes

class Engine:
    def __init__(self, projSettings):

        self.projSettings = projSettings

        self.frameCount = 0

    def Init(self):

        self.renderer = RenderMod.Renderer(self.projSettings)
        self.renderer.Init()

        self.scene = SceneMod.Scene("scene1")
        self.scene.Load()

    def Update(self, deltaTime, stableDTime):

        exitCode = True
        
        self.renderer.Clear()

        inputList = []

        for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        exitCode = False
                    if event.type == pygame.KEYDOWN:
                        inputList.append(chr(event.key))

        self.scene.Update(deltaTime, inputList)
        
        for obj in self.scene.objs:
            geometry, luminance = obj.getViewSpaceGeometry(self.projSettings, self.scene.camera)

            #print(geometry)
            #print("drawing")
            for i in range(len(geometry)):
                #print(face)
                #print("g : " + str(geometry[i]))
                #print(geometry[i][0])
                self.renderer.DrawTri(geometry[i][0], geometry[i][1], geometry[i][2], luminance[i])
                #self.renderer.Draw(face[1], face[2])
                #self.renderer.Draw(face[2], face[0])
                
        self.frameCount += 1
        self.renderer.Show(stableDTime)

        return exitCode
