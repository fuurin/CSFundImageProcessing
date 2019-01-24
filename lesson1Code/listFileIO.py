def readStringListFromFile(fileName):

    readList=[]
    with open(fileName) as file:
        for line in file:
            readList.append(line.rstrip())
    return readList

def readIntListFromFile(fileName):

    readList=[]
    with open(fileName) as file:
        for line in file:
            readList.append(int(line.rstrip()))
    return readList

def readFloatListFromFile(fileName):

    readList=[]
    with open(fileName) as file:
        for line in file:
            readList.append(float(line.rstrip()))
    return readList


if __name__=="__main__":

    print("OUTPUT1: "+str(readFloatListFromFile("input1.txt")))
