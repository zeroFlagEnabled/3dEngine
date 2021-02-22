#Object

#IMPORTATIONS

import MatrixMod
import NormalMod
import AlgoMod

#Classes

class Mesh:
    def __init__(self, vertexPool, faceMap):
        
        self.vertexPool = vertexPool
        #print(self.vertexPool)
        self.faceMap = faceMap
        #print(faceMap)

    def Update(self, vertexPool):
        self.vertexPool = vertexPool
        #print("mesh updated")
        #print(vertexPool[0])

class Prefab:
    def __init__(self, name):

        self.name = name
    
    def Define(self, vertexPool, faceMap):
        
        self.mesh = Mesh(vertexPool, faceMap)
        #print(self.name)
        #print(self.mesh.vertexPool)

    def ReadOut(self):

        print("prefab(" + self.name+ ")")

        for face in self.mesh.faceMap:
            for vertex in face:
                print(self.mesh.vertexPool[vertex])

class Obj(Prefab):
    def RawDefine(self, vertexPool, faceMap, position, rotation, scale):

        self.worldMesh = Mesh(vertexPool, faceMap)
        self.pos = position
        self.rot = rotation
        self.scale = scale

    def Define(self, prefab, position, rotation, scale):

        self.worldMesh = prefab.mesh
        self.modelMesh = Mesh(tuple(self.worldMesh.vertexPool), self.worldMesh.faceMap)
        #print(prefab.name)
        #print(prefab.mesh.vertexPool)
        self.pos = position
        self.rot = rotation
        self.scale = scale

        self.worldMesh.Update(MatrixMod.physMat(self, self.pos, self.rot, self.scale))

    def Update(self, position, rotation, scale):

        newPos = []
        newRot = []
        newScale = []
        

        for i in range(3):
            #print(i)
            newPos.append(position[i] + self.pos[i])
            newRot.append(rotation[i] + self.rot[i])
            newScale.append(scale[i] + self.scale[i])
        
        self.pos = newPos
        self.rot = newRot
        self.scale = newScale

        #print(newPos)
        #print(newRot)

        #print("model mesh")
        #print(self.modelMesh.vertexPool[0])

        self.worldMesh.Update(MatrixMod.physMat(self, self.pos, self.rot, self.scale))
        
    def ReadOut(self):

        print("obj(" + self.name + ")")

        print("position : ")
        print(self.pos)
        print("rotation : ")
        print(self.rot)
        print("scale : ")
        print(self.scale)

        #print(self.worldMesh.faceMap)

        for face in self.worldMesh.faceMap:
            for vertex in face:
                print(self.worldMesh.vertexPool[vertex])
                
    def getGeometry(self):

        geometry = []

        for face in self.worldMesh.faceMap:
            geometry.append([self.worldMesh.vertexPool[face[0]], self.worldMesh.vertexPool[face[1]], self.worldMesh.vertexPool[face[2]]]) 

        return geometry
    
    def getViewSpaceGeometry(self, projSettings):

        self.worldMesh.faceMap = AlgoMod.Painters(self.worldMesh)

        viewSpaceMesh = Mesh(MatrixMod.viewSpaceMat(self, projSettings), self.worldMesh.faceMap)

        geometry = []
        luminance = []

        for face in viewSpaceMesh.faceMap:
            viewVertexList = [viewSpaceMesh.vertexPool[face[0]], viewSpaceMesh.vertexPool[face[1]], viewSpaceMesh.vertexPool[face[2]]]
            #print("bh " + str(viewVertexList))
            worldVertexList = [self.worldMesh.vertexPool[face[0]], self.worldMesh.vertexPool[face[1]], self.worldMesh.vertexPool[face[2]]]
            
            renderInfo = NormalMod.RenderInfo(worldVertexList)
            if renderInfo[0]:
                geometry.append(viewVertexList)
                luminance.append(renderInfo[1])

        return geometry, luminance

#vP = [[0,1,2],[3,4,5],[6,7,8],[9,10,11]]
#fM = [[0,1,2],[1,2,3]]

#obj = Obj()
#obj.Define(vP, fM)
#obj.ReadOut()
