import random

def createRandom3DPoint(minV=-1,maxV=1):
    x=round(random.uniform(minV,maxV),3)
    y=round(random.uniform(minV,maxV),3)
    z=round(random.uniform(minV,maxV),3)
    return (x,y,z)

def createRandomPointList(numPoints=10):
    returnList=[]
    for i in range(numPoints):returnList.append(createRandom3DPoint())
    return returnList   

if __name__=="__main__":

    numberOfPoints=15
    listOfPoints1=createRandomPointList(numberOfPoints)
    
    print("the first list created was "+str(listOfPoints1))


