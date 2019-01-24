import time
import sys
import random
from hakyuuPlayer import playerQualities
from hakyuuPlayer import hPlayer
import hakyuuPlayerIO as hIO

#1) Iterating Dictionares
print("\n\n\n\n\n\n Creating a bunch of Hakyuu players:")

playersDict={}
numPlayers=1000

playerNames=['randomGuy','Yago','Hinata','Sawamura','Azumane','Shimizu','Tokuyama','Tanaka','Narita','Ennoshita','Kinoshita','Tobio','Tsuishima','Yamaguchi','Haraguchi','Yachi','Ukai','Takeda','Kuroo','Kai','Rakuten','Kozume','Yamamoto','Fukunaga','Inuoka','Bowser','Shibayama','Haiba','Nekomata','Naoi','Toru','Yakiniku','Shizuku','Hajime','Hanamaki','Matsukawa','Yahaba','Watari','Kyoutani','Kunimi','Kitayama','Irihata','Mizoguchi']
teamNames=['Karasuno','Nekoma','Fukuroudani','Aoba Jousai','Date','Tateko']

#In this example we will measure clock time
start = time.time()

#for each element
for i in range(numPlayers):
    #choose a player Name randomly from the list
    playerNameNumber=random.randint(0,len(playerNames)-1)

    #choose a team randomly from the list
    teamNumber=random.randint(0,len(teamNames)-1)

    #if i%100000==0: print " now at "+str(i)
    player=hIO.createRandomPlayer(playerNames[playerNameNumber]+str(i), round(random.uniform(170,210),2),teamNames[teamNumber])

    # Add to the dictionary, the name and the player is the value
    playersDict[player.name]=player
end = time.time()

print("finished data generation in (TIME 1) "+str(end - start))

#In this example we will measure clock time
start = time.time()

#now let's iterate over all elements by using index, every element in the dictionary gets broken into key and value
for key,value in playersDict.items():
    print("player "+key+" from team "+value.team+" has height "+str(value.height))

end = time.time()

print("finished iterating the dictionary in (TIME 2) "+str(end - start))



# Now let us create a dictionary for every particular position
#now let's iterate over all elements by using index, every element in the dictionary gets broken into key and value
middleBlockers={}
liberos={}
setters={}
wingSpikers={}
defenders={}
centralBacks={}

for key,value in playersDict.items():
    # distribute every player on th dictionary corresponding to their position
    if(value.position=='mb'):middleBlockers[value.name]=value
    elif (value.position=='ws'):wingSpikers[value.name]=value
    elif (value.position=='s'):setters[value.name]=value
    elif (value.position=='lib'):liberos[value.name]=value
    elif (value.position=='cb'):centralBacks[value.name]=value
    elif (value.position=='d'):defenders[value.name]=value
end = time.time()

print("finished creating position based dictionaries in (TIME 2) "+str(end - start))

print("out of a total of "+str(len(playersDict))+" players, there are, Wing Spikers: "+str(len(wingSpikers))+" middle blockers "+str(len(middleBlockers))+" setters "+str(len(setters))+" defenders "+str(len(defenders))+" centralBacks "+str(len(centralBacks))+" liberos "+str(len(liberos)))


#now we can check easily, for example, who the tallest middle blocker is
tallest=-1
for key,value in middleBlockers.items():
    if(value.height>tallest):
        tallestPlayer=value
        tallest=value.height

print("the tallest middle blocker is "+str(tallestPlayer))
