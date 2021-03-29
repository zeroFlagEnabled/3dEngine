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

        self.modelSpaceMesh = Mesh(vertexPool, faceMap)
        self.pos = position
        self.rot = rotation
        self.scale = scale

    def Define(self, prefab, position, rotation, scale):

        #self.worldMesh = prefab.mesh
        #self.modelSpaceMesh = Mesh(tuple(self.worldMesh.vertexPool), self.worldMesh.faceMap)
        self.modelSpaceMesh = prefab.mesh
        #print(prefab.name)
        #print(prefab.mesh.vertexPool)
        self.pos = position
        self.rot = rotation
        self.scale = scale

        #self.worldMesh.Update(MatrixMod.physMat(self, self.pos, self.rot, self.scale))

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

        #self.worldMesh.Update(MatrixMod.physMat(self, self.pos, self.rot, self.scale))
        
    def ReadOut(self):

        print("obj(" + self.name + ")")

        print("position : ")
        print(self.pos)
        print("rotation : ")
        print(self.rot)
        print("scale : ")
        print(self.scale)

        #print(self.worldMesh.faceMap)

        for face in self.modelSpaceMesh.faceMap:
            for vertex in face:
                print(self.modelSpaceMesh.vertexPool[vertex])
                
    def getGeometry(self):

        geometry = []

        for face in self.modelSpaceMesh.faceMap:
            geometry.append([self.modelSpaceMesh.vertexPool[face[0]],
                             self.modelSpaceMesh.vertexPool[face[1]],
                             self.modelSpaceMesh.vertexPool[face[2]]]) 

        return geometry
    
    def getViewSpaceGeometry(self, projSettings, camera):

        worldSpaceMesh = Mesh(MatrixMod.physMat(self, self.pos, self.rot, self.scale), self.modelSpaceMesh.faceMap)

        cameraSpaceMesh = Mesh(MatrixMod.cameraSpaceMat(self, camera), worldSpaceMesh.faceMap)

        cameraSpaceMesh.faceMap = AlgoMod.Painters(cameraSpaceMesh)
        
        facesToProject = []
        luminance = []

        for face in worldSpaceMesh.faceMap:
            cameraVertexPool = [cameraSpaceMesh.vertexPool[face[0]],
                               cameraSpaceMesh.vertexPool[face[1]],
                               cameraSpaceMesh.vertexPool[face[2]]]


            renderInfo = NormalMod.RenderInfo(cameraVertexPool, camera)
            if renderInfo[0]:
                facesToProject.append(cameraVertexPool)
                luminance.append(renderInfo[1])

        facesToRender = MatrixMod.viewSpaceMat(facesToProject, projSettings)
        #print(facesToRender)
        #print("faces") 


        """

        viewSpaceMesh = Mesh(MatrixMod.viewSpaceMat(worldSpaceMesh, projSettings), worldSpaceMesh.faceMap)

        geometry = []
        luminance = []

        for face in viewSpaceMesh.faceMap:
            viewVertexList = [viewSpaceMesh.vertexPool[face[0]], viewSpaceMesh.vertexPool[face[1]], viewSpaceMesh.vertexPool[face[2]]]
            #print("bh " + str(viewVertexList))
            worldVertexList = [worldSpaceMesh.vertexPool[face[0]],
                               worldSpaceMesh.vertexPool[face[1]],
                               worldSpaceMesh.vertexPool[face[2]]]
            
            renderInfo = NormalMod.RenderInfo(worldVertexList)
            if renderInfo[0]:
                geometry.append(viewVertexList)
                luminance.append(renderInfo[1])
        """

        return facesToRender, luminance

#vP = [[0,1,2],[3,4,5],[6,7,8],[9,10,11]]
#fM = [[0,1,2],[1,2,3]]

#obj = Obj()
#obj.Define(vP, fM)
#obj.ReadOut()
