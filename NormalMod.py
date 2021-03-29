#NormalMod

import numpy as np

def Normalize(vector):
    
    #norm = np.linalg.norm(vector)
    norm = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    #print("norm : " + str(norm))
    #print("to be normalized : " + str(vector))
    #print(normal, norm)
    #vector[0] = float(vector[0]) / norm
    #vector[1] = float(vector[1]) / norm
    #vector[2] = float(vector[2]) / norm
    vector = vector / norm
    #print("normalized" + str(vector))

    return vector

def CalculateNormal(vector1, vector2):
    normal = np.cross(vector1, vector2)
    #print("cross : " + str(normal))

    normal = Normalize(normal)

    return normal
    
def RenderInfo(vertexList, camera):

    #print(vertexList)
    
    vector1 = np.array([float(vertexList[1][0] - vertexList[0][0]), float(vertexList[1][1] - vertexList[0][1]), float(vertexList[1][2] - vertexList[0][2])])
    #print("vector1 : " + str(vector1))
    vector2 = np.array([float(vertexList[2][0] - vertexList[1][0]), float(vertexList[2][1] - vertexList[1][1]), float(vertexList[2][2] - vertexList[1][2])])
    #print("vector2 : " + str(vector2))

    #vector1 = np.array([vertexList[1][0] - vertexList[2][0], vertexList[1][1] - vertexList[2][1], vertexList[1][2] - vertexList[2][2]])
    #vector2 = np.array([vertexList[0][0] - vertexList[1][0], vertexList[0][1] - vertexList[1][1], vertexList[0][2] - vertexList[1][2]])
    
    #castingVector = np.array(vertexList[0]) - np.array(camera.vec)
    castingVector = np.array(vertexList[0])
    lightingVector = Normalize(np.array([0,0,1]))
    #lightingVector = np.array([0,0,1])
    normal = CalculateNormal(vector1, vector2)
    #normal = np.array([0,0.99,0.01])
    
    #print("castingVector" + str(castingVector))
    #print("normal : " + str(normal))
    #print(castingVector.dot(normal))
    if castingVector.dot(normal) < 0.0:
    #if True:
        renderInfo = [True, - normal.dot(lightingVector), vertexList]
        #renderInfo = [True, normal.dot(lightingVector)]
        #print("normal " + str(normal))
        #print("face " + str(vertexList))
        #print(normal.dot(lightingVector))
    else:
        renderInfo = [False]

    return renderInfo

#vertexList = [[0,0,1],[0,1,1],[1,0,1]]
#vertexList = [[1,0,1],[0,1,1000],[0,0,1]]
#vertexList2 = [[1,0,1],[0,1,1],[0,0,1]]
#vertexList = [[0,0,1],[0,0,2],[1,0,1]]
#print(RenderInfo(vertexList))
#print(RenderInfo(vertexList2))

    
