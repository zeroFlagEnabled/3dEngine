#NormalMod

import numpy as np

def Normalize(vector):
    
    norm = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    vector = vector / norm

    return vector

def CalculateNormal(vector1, vector2):
    normal = np.cross(vector1, vector2)
    normal = Normalize(normal)

    return normal
    
def RenderInfo(vertexList):

    """ Tout le système de base, permet grace aux normales de déterminer si une face doit être rendue ou pas """
    
    vector1 = np.array([float(vertexList[1][0] - vertexList[0][0]), float(vertexList[1][1] - vertexList[0][1]), float(vertexList[1][2] - vertexList[0][2])])
    vector2 = np.array([float(vertexList[2][0] - vertexList[1][0]), float(vertexList[2][1] - vertexList[1][1]), float(vertexList[2][2] - vertexList[1][2])])

    castingVector = np.array(vertexList[0]) #needs to be changed when camera moves
    lightingVector = Normalize(np.array([0,0,1]))
    normal = CalculateNormal(vector1, vector2)

    if castingVector.dot(normal) < 0.0:
        renderInfo = [True, - normal.dot(lightingVector), vertexList]
    else:
        renderInfo = [False]

    
    """
    #Sans détermination par normales
    
    vector1 = np.array([float(vertexList[1][0] - vertexList[0][0]), float(vertexList[1][1] - vertexList[0][1]), float(vertexList[1][2] - vertexList[0][2])])
    vector2 = np.array([float(vertexList[2][0] - vertexList[1][0]), float(vertexList[2][1] - vertexList[1][1]), float(vertexList[2][2] - vertexList[1][2])])

    castingVector = np.array(vertexList[0]) #needs to be changed when camera moves
    lightingVector = Normalize(np.array([0,0,1]))
    #normal = CalculateNormal(vector1, vector2)
    renderInfo = [True, 1, vertexList]
    """

    return renderInfo 


#vertexList = [[0,0,1],[0,1,1],[1,0,1]]
#vertexList = [[1,0,1],[0,1,1000],[0,0,1]]
#vertexList2 = [[1,0,1],[0,1,1],[0,0,1]]
#vertexList = [[0,0,1],[0,0,2],[1,0,1]]
#print(RenderInfo(vertexList))
#print(RenderInfo(vertexList2))

    
