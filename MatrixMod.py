#Matrix

#IMPORTATIONS

import numpy as np

# Matrices 2D

def rot2D(theta):
    mat = np.array([[np.cos(theta),np.sin(theta)],[-np.sin(theta),np.cos(theta)]])
    return mat

# Matrices 3D

def rotXMat(rot):
    #print(rot)
    theta = np.radians(rot[0])
    #print("thetaX = " + str(theta))
    mat = np.array([[1,0,0,0],[0,np.cos(theta),np.sin(theta),0],[0,-np.sin(theta),np.cos(theta),0],[0,0,0,1]])
    #print("Xmat")
    #print(mat)
    return mat

def rotYMat(rot):
    theta = np.radians(rot[1])
    #print("thetaY = " + str(theta))
    mat = np.array([[np.cos(theta),0,-np.sin(theta),0],[0,1,0,0],[np.sin(theta),0,np.cos(theta),0],[0,0,0,1]])
    #print("Ymat")
    #print(mat)
    return mat

def rotZMat(rot):
    theta = np.radians(rot[2])
    #print("thetaZ = " + str(theta))
    mat = np.array([[np.cos(theta),np.sin(theta),0,0],[-np.sin(theta),np.cos(theta),0,0],[0,0,1,0],[0,0,0,1]])
    #print("Zmat")
    #print(mat)
    return mat

def scaleMat(scale):
    x = scale[0]
    y = scale[1]
    z = scale[2]
    mat = np.array([[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]])
    return mat

def transMat(pos):
    x = pos[0]
    y = pos[1]
    z = pos[2]
    mat = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[x,y,z,1]])
    #print("trans")
    #print(mat)
    return mat

def projMat(projSettings):
    aR = projSettings["aspectRatio"]
    f = 1/np.tan(np.radians(projSettings["fov"])/2)
    #q = projSettings["zFar"]/(projSettings["zFar"] - projSettings["zNear"])
    q = 1/(projSettings["zFar"] - projSettings["zNear"])
    zNear = projSettings["zNear"]
    mat = np.array([[aR * f,0,0,0],[0,f,0,0],[0,0,q,-(zNear * q)],[0,0,1,0]])
    return mat

# Opérations

def physMat(obj, position, rotation, scale):
    result = []

    #rotated = rotZMat(rotation).dot(rotYMat(rotation).dot(rotXMat(rotation)))
    #scaled = scaleMat(scale).dot(rotated)
    #physMat = transMat(position).dot(scaled)
    
    translated = transMat(position)
    scaled = scaleMat(scale).dot(translated)
    physMat = rotXMat(rotation).dot(rotYMat(rotation).dot(rotZMat(rotation).dot(scaled)))


    #print("physMat")
    #print(physMat)
    
    for vertex in obj.modelMesh.vertexPool:
        
        vector = np.array(vertex)
        vector = np.append(vector, 1)
        product = vector.dot(physMat)
        #product = physMat.dot(vector)
        #print("vertex")
        #print(vertex)
        #print("product")
        #print(product)
        newVertex = product.tolist()
        newVertex.pop()
        result.append(newVertex)
    return result
        
        
        
def viewSpaceMat(obj, projSettings):

    # Could be more efficient by calculating projMat once
    
    result = []
    for vertex in obj.worldMesh.vertexPool:

        #print(vertex)
        
        vector = np.array(vertex)
        vector = np.append(vector, 1)
        #product = vector.dot(projMat(projSettings))
        product = projMat(projSettings).dot(vector)
        newVertex = product.tolist()

        if newVertex[3] != 0:
            newVertex[0] /= newVertex[3]
            newVertex[1] /= newVertex[3]
            newVertex[2] /= newVertex[3]

        #print("normalized")
        #print(newVertex)

        # Scaling into view

        newVertex[0] = (newVertex[0] + 1.0) / 2 * projSettings["width"]
        newVertex[1] = (-newVertex[1] + 1.0) / 2 * projSettings["height"]
        newVertex[2] = (newVertex[2] + 1.0) / 2 * projSettings["width"]

        #print("scaled")
        #print(newVertex)

        

        newVertex.pop()
        result.append(newVertex)
    return result

#v = np.array([1,0])
#r = rot2D(np.pi)
#print(r)
#print(r.dot(v))

    

