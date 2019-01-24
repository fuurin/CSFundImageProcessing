import collections
from hakyuuPlayer import playerQualities
from hakyuuPlayer import hPlayer
import random 

def modifyRandomly(fValue, percentage):
    return fValue**round(random.uniform(1-1*float(percentage)/100,1+1*float(percentage)/100 ),3)

def createRandomPlayer(nameInit="noname",heightInit=180.5,teamInit="NOTEAM",positionInit="noPOS",powerInit=-1,springInit=-1,staminaInit=-1,brainInit=-1,techniqueInit=-1,speedInit=-1):
    if(powerInit==-1):powerInit=random.randint(1, 5)
    if(springInit==-1):springInit=random.randint(1, 5)
    if(staminaInit==-1):staminaInit=random.randint(1, 5)
    if(brainInit==-1):brainInit=random.randint(1, 5)
    if(techniqueInit==-1):techniqueInit=random.randint(1, 5)
    if(speedInit==-1):speedInit=random.randint(1, 5)

    possiblePositions=["ws","mb","s","d","cb","lib"]
    if(positionInit=="noPOS"):positionInit=possiblePositions[random.randint(0,len(possiblePositions)-1)]
    
    randomGuy= hPlayer(name=nameInit, height=heightInit, team=teamInit, position=positionInit,qualities=playerQualities(powerInit,springInit,staminaInit,brainInit,techniqueInit,speedInit) )

    return randomGuy

#receives a file that has already been open in fileHandle
def writePlayerToFile(fileHandle,player):
    fileHandle.write(player.name+"\n")
    fileHandle.write(str(player.height)+"\n")
    fileHandle.write(player.team+"\n")
    fileHandle.write(player.position+"\n")
    fileHandle.write(str(player.qualities.power)+"\n")
    fileHandle.write(str(player.qualities.spring)+"\n")
    fileHandle.write(str(player.qualities.stamina)+"\n")
    fileHandle.write(str(player.qualities.brain)+"\n")
    fileHandle.write(str(player.qualities.technique)+"\n")
    fileHandle.write(str(player.qualities.speed)+"\n")
    
#receives a file that has already been open in fileHandle
def readPlayerFromFile(fileHandle):
    nameInit=fileHandle.readline().strip()
    heightInit=float(fileHandle.readline().strip())
    teamInit=fileHandle.readline().strip()
    positionInit=fileHandle.readline().strip()
    powerInit=int(fileHandle.readline().strip())
    springInit=int(fileHandle.readline().strip())
    staminaInit=int(fileHandle.readline().strip())
    brainInit=int(fileHandle.readline().strip())
    techniqueInit=int(fileHandle.readline().strip())
    speedInit=int(fileHandle.readline().strip())
    return hPlayer(name=nameInit, height=heightInit, team=teamInit, position=positionInit,qualities=playerQualities(powerInit,springInit,staminaInit,brainInit,techniqueInit,speedInit) )

