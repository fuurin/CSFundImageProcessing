import random
import sys
from .pokemonDef import Monster,superEffective,notEffective,noEffect

def ResetHP(pokemon):
    pokemon.hitpoint[1]=pokemon.hitpoint[0]

def readPokemonFromLine(line, index):
    #number, number hp, attack, defense, sp attack, sp defense, speed, total, average
    readList=line.split(" ")
    return Monster(name=readList[2], index=index, attack=int(readList[4]), defense=int(readList[5]), speed=int(readList[7]), hitpoint=[int(readList[3]),int(readList[3])], variety=[])

def readPokemonListFromFile(filename):
    #returns a list of Pokemons read from the file
    readList=[]
    index = 0
    with open(filename) as file:
        for line in file:
            readList.append(readPokemonFromLine(line, index=index))
            index += 1
    file.close()
    return readList

def readPokemonTypeFromLine(line):
    #number, number name name types
    readList=line.split(" ")
    typeList=[]
    
    # Lines with 2 #s have week point types. So they should be ignored
    if readList[1][0] != '#': return(readList[2], typeList)
    
    for i in range(4,len(readList)):
        typeList.append(readList[i].rstrip())
    #print("pokemon "+str(readList[2])+" has type(s) "+str(typeList))
    return (readList[2],typeList )

def readPokemonTypesFromFile(filename):
    #returns a liat of Pokemons read from the file
    readList=[]
    with open(filename) as file:
        for line in file:
            readList.append(readPokemonTypeFromLine(line))
    file.close()
    return readList


#returns 0 if Pokemon1 wins, 1 if Pokemon2 wins and 2 if there is a draw
def battle(Pokemon1, Pokemon2,verbose=False,resetHP=True):
    #First, make sure that both contenders are rested, replenish their HPs
    #Pokemons rest for the next battle and replenish HP
    if(resetHP):
        ResetHP(Pokemon1)
        ResetHP(Pokemon2)

    if(verbose):print (""+str(Pokemon1.name)+"'s ability is\n\tHP = "+str(Pokemon1.hitpoint)+"\n\tattack = "+str(Pokemon1.attack)+"\n\tdefense = "+str(Pokemon1.defense)+"\n\tspeed = "+str(Pokemon1.speed)+"\n\ttype = "+str(Pokemon1.variety)+"")
    if(verbose):print (""+str(Pokemon2.name)+"'s ability is\n\tHP = "+str(Pokemon2.hitpoint)+"\n\tattack = "+str(Pokemon2.attack)+"\n\tdefense = "+str(Pokemon2.defense)+"\n\tspeed = "+str(Pokemon2.speed)+"\n\ttype = "+str(Pokemon2.variety)+"")

    randomMargin=0.2
    effectiveness=0.3

    #compute attack centers
    attackCenter1=1
    if superEffective(Pokemon1, Pokemon2):
        if(verbose):print(Pokemon1.name+" is super Effective against "+Pokemon2.name)
        attackCenter1+=effectiveness
    if notEffective(Pokemon1, Pokemon2):
        if(verbose):print(Pokemon1.name+" is not very Effective against "+Pokemon2.name)
        attackCenter1-=effectiveness
    if noEffect(Pokemon1, Pokemon2):
        if(verbose):print(Pokemon1.name+" has no Effect against "+Pokemon2.name)
        attackCenter1=-0.5

    attackCenter2=1
    if superEffective(Pokemon2, Pokemon1):
        if(verbose):print(Pokemon2.name+" is super Effective against "+Pokemon1.name)
        attackCenter2+=effectiveness
    if notEffective(Pokemon2, Pokemon1):
        if(verbose):print(Pokemon2.name+" is not very Effective against "+Pokemon1.name)
        attackCenter2-=effectiveness
    if noEffect(Pokemon2, Pokemon1):
        if(verbose):print(Pokemon2.name+" has no Effect against "+Pokemon1.name)
        attackCenter2=-0.5

    if noEffect(Pokemon1, Pokemon2) and noEffect(Pokemon2, Pokemon1):
        if(verbose):print("These two pokemon cannot hurt each other, draw! ")
        return 2

    rounds=0
    maxRounds=100
    while Pokemon1.hitpoint[1]>0 and Pokemon2.hitpoint[1]>0 and rounds<maxRounds:

        speed1=Pokemon1.speed*round(random.uniform(0.8,1.2),3)
        speed2=Pokemon2.speed*round(random.uniform(0.8,1.2),3)

        attack1=Pokemon1.attack*round(random.uniform(attackCenter1-randomMargin,attackCenter1+randomMargin),3)
        attack2=Pokemon2.attack*round(random.uniform(attackCenter2-randomMargin,attackCenter2+randomMargin),3)

        defense1=Pokemon1.defense*round(random.uniform(0.7,1.1),3)
        defense2=Pokemon2.defense*round(random.uniform(0.7,1.1),3)

        #Compute possible damages
        #damage mustn't be a negative number, so if damage is a negative number, damage becomes zero
        damage1=int(attack2-defense1)
        if (damage1<0): damage1=0

        damage2=int(attack1-defense2)
        if (damage2<0): damage2=0

        #fastest monster attacks first:
        if (speed1>speed2):
            Pokemon2.hitpoint[1]=Pokemon2.hitpoint[1]-damage2
            if(verbose):print ("\n"+str(Pokemon2.name)+" received "+str(damage2)+" damage from "+str(Pokemon1.name)+" and has remaining HP "+str(Pokemon2.hitpoint[1]))
            if Pokemon2.hitpoint[1]>0:
                #the fight continues
                Pokemon1.hitpoint[1]=Pokemon1.hitpoint[1]-damage1
                if(verbose):print ("\n"+str(Pokemon1.name)+" received "+str(damage1)+" damage from  "+str(Pokemon2.name)+" and has remaining HP "+str(Pokemon1.hitpoint[1]))
        else:
            Pokemon1.hitpoint[1]=Pokemon1.hitpoint[1]-damage1
            if(verbose):print ("\n"+str(Pokemon1.name)+" received "+str(damage1)+" damage from "+str(Pokemon2.name)+" and has remaining HP "+str(Pokemon1.hitpoint[1]))
            if Pokemon1.hitpoint[1]>0:
                #the fight continues
                Pokemon2.hitpoint[1]=Pokemon2.hitpoint[1]-damage2
                if(verbose):print ("\n"+str(Pokemon2.name)+" received "+str(damage2)+" damage from  "+str(Pokemon1.name)+" and has remaining HP "+str(Pokemon2.hitpoint[1]))
        rounds=rounds+1

    #Combat is finished, check who won
    if rounds==maxRounds:
        if(verbose):print("Round limit reached, draw! ")
        return 2
    else:
        if (Pokemon1.hitpoint[1]>0):
            #Pokemons rest for the next battle and replenish HP
            if(verbose):print ("\n"+str(Pokemon1.name)+" wins the battle.")
            return 0
        else:
            if(verbose):print ("\n"+str(Pokemon2.name)+" wins the battle.")
            return 1
