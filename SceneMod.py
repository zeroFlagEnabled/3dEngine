#Scene

#IMPORTATIONS

import os

import ObjectMod

#Classes

class Scene:
    def __init__(self, directory):
        
        self.directory = directory

        self.fileList = []
        with os.scandir("./" + self.directory + "/") as referenceList:
            for item in referenceList:
                if item.name != "stagerFile.txt":
                    self.fileList.append(item.name)

    def setObjID(self, ID, num =0):
        
        if num != 0:
            tempID = ID + str(num)
        else:
            tempID = ID

        for item in list(self.stage):
            if tempID == item:
                return self.setObjID(ID, num+1)
        return tempID
                    
    def LoadStagerFile(self):
        
        self.stage = {}
        with open("./" + self.directory + "/stagerFile.txt", "r") as stagerFile:
            content = stagerFile.readlines()
            for line in content:
                if line[0] == "o":
                    wordsInLine = line.split(" ")
                    self.stage[self.setObjID(wordsInLine[1])] = wordsInLine[2:]
        self.stageList = list(self.stage)
                    
    def LoadPrefabFile(self, prefabName):

        vertexPool = []
        faceMap = []
            
        with open("./" + self.directory + "/" + prefabName, "r") as prefabFile:
            content = prefabFile.readlines()
            for line in content:
                if line[0] == "v":
                    wordsInLine = line.split(" ")
                    vertexPool.append([float(wordsInLine[1]), float(wordsInLine[2]), float(wordsInLine[3])])
                elif line[0] == "f":
                    wordsInLine = line.split(" ")
                    faceMap.append([int(wordsInLine[1]) - 1, int(wordsInLine[2]) - 1, int(wordsInLine[3]) - 1])

        prefab = ObjectMod.Prefab(prefabName)
        prefab.Define(vertexPool, faceMap)

        vertexPool = []
        faceMap = []

        return prefab

    def Load(self):

        self.LoadStagerFile()

        self.prefabs = []
       
        for prefabName in self.fileList:
            self.prefabs.append(self.LoadPrefabFile(prefabName))

        self.objs = []

        for obj in self.stageList:
            self.objs.append(ObjectMod.Obj(obj))
            #print("position : " + str(self.stage[obj][1] + str(self.stage[obj][2] + str(self.stage[obj][3]))
            #print("position : " + str(self.stage[obj][1] + str(self.stage[obj][2] + str(self.stage[obj][3]))
            position = [float(self.stage[obj][1]), float(self.stage[obj][2]), float(self.stage[obj][3])]
            rotation = [float(self.stage[obj][4]), float(self.stage[obj][5]), float(self.stage[obj][6])]
            scale = [float(self.stage[obj][7]), float(self.stage[obj][8]), float(self.stage[obj][9])]

            objPrefab = 0
            
            for prefab in self.prefabs:
                if prefab.name == self.stage[obj][0]:
                    objPrefab = prefab
            if objPrefab == 0:
                print("ERROR: Prefab referenced in stagerFile doesn't exist")

            self.objs[-1].Define(objPrefab, position, rotation, scale)
            #self.objs[-1].ReadOut()
     
    def Unload(self):
        pass

    def Update(self):
        self.objs[0].Update([0,0,0], [0,0.5,0], [0,0,0])
        #self.objs[1].Update([0,0,0], [0,0.5,0], [0,0,0])
        #self.objs[2].Update([0,0,0], [0,0.5,0], [0,0,0])
            
