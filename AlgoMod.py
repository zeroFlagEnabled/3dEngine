#Algorithm

def TriCenter(tri):
    
    centerPoint = [0,0,0]
    centerPoint[0] = (tri[0][0] + tri[1][0] + tri[2][0])/3.0
    centerPoint[1] = (tri[0][1] + tri[1][1] + tri[2][1])/3.0
    centerPoint[2] = (tri[0][2] + tri[1][2] + tri[2][2])/3.0

    #print(centerPoint)

    return centerPoint

def ZVal(tri):
    centerVertex = TriCenter(tri)

    return centerVertex[2]

def Painters(mesh):
    
    #print("newFrame")
    
    #print("g1 " + str(geometry))

    #for i in range(len(viewSpaceGeometry)):
        #viewSpaceGeometry.append()
        #print("tri" + str(viewSpaceGeometry[i]))
    #print(geometry)

    sortedfaceMap = sorted(mesh.faceMap, key = lambda tri : ZVal([mesh.vertexPool[tri[0]],
                                                                  mesh.vertexPool[tri[1]],
                                                                  mesh.vertexPool[tri[2]]]), reverse = True)

    return sortedfaceMap

"""
    viewSpaceGeometry = []

    for tri in sortedGeometry:
        #print("f " +str(tri[0]))
        viewSpaceGeometry.append(tri[0])
        #print("tri " + str(tri[1]))
        
        #print("ZVal " + str(ZVal(tri[1])))
        
        #viewSpaceGeometry.append(tri[0][1])
        #viewSpaceGeometry.append(tri[0][2])

    #print("geo : " + str(viewSpaceGeometry))

    #print("g2 " + str(viewSpaceGeometry[1]))

"""
#[[[1],[1],[1]],[[0,0,0],[0,1,0], [1,0,0], [[[0,0,1],[0,1,1], [1,0,1]], [0,0,2],[0,1,2], [1,0,2]]]
#geo = [[[[[1]],[[0,0,0], [0,1,0], [1,0,0]], [[0,0,1],[0,1,1], [1,0,1]], [[0,0,2],[0,1,2], [1,0,2]]]]
#sortGeo = Painters(geo)
