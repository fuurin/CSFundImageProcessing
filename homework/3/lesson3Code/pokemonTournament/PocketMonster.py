#import collections
from .pokemonDef import Monster
import pokemonFunctions as pf
import sys
import random

#First, read all the pokemon types and put them in a list of tuples (name, listOfTypes).
listOfNamesAndTypes=pf.readPokemonTypesFromFile("listOfPokemon1.txt")

# Then, read all pokemon from a file and put them on a list (the types are not correctly updated)
pokeList=pf.readPokemonListFromFile("listOfPokemon2.txt")
#print "length of the list "+str(len(pokeList))+" "+str(pokeList)

#TASK A, put all pokemon in the list in a dictionary where the key is the name of the pokemon
pokedex={}
# Put all pokemon in a dictionary by name
for monster in pokeList:
    pokedex[monster.name]=monster

#TASK B, put go over listOfNamesAndTypes, for every pokemon there, update its types, look for it in the pokedex dictionary and append the types to list pokedex[name].variety
for name,listOfTypes in listOfNamesAndTypes:
    #print "updating types for  "+name
    for t in listOfTypes:
        pokedex[name].variety.append(t)

#Did the monsters in list pokeList also get their names updated? Why?
print(pokedex["Bulbasaur"])
print(pokeList[0])

#now we can make monsters fight by doing:
#pf.battle(pokedex["Bulbasaur"],pokedex['Charmander'])
#or also
#pf.battle(pokeList[8],pokeList[137])

#random battle
fighter1=random.randint(0,len(pokeList)-1)
fighter2=random.randint(0,len(pokeList)-1)
winner=pf.battle(pokeList[fighter1],pokeList[fighter2],True)
