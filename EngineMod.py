#Engine module

#IMPORTATIONS

import RenderMod
import SceneMod
import MatrixMod

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

    def Update(self, deltaTime):
        
        self.renderer.Clear()

        self.scene.Update()
        
        for obj in self.scene.objs:
            geometry, luminance = obj.getViewSpaceGeometry(self.projSettings)

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
        self.renderer.Show(deltaTime)
