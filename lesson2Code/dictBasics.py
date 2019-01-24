import time
import random

#1) Define our first dictionary
phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052,
}
# Print an entry using the key to access it
print("Dictionary example 1, accessing an element "+str(phonebook["bob"]))

#iterate over all elements
for dict_key, dict_value in phonebook.items():
    print(dict_key,'->',dict_value)

#2) Dictionary efficiency
# Now we will see the difference between accessing pairs in a list and a dictionary:
# create list and dictionary
print("\n\n\n\n\n\n Dictionary example 2, dictionary efficiency")

largeDict={}
largeList=[]

numElements=50000
#In this example we will measure clock time
start = time.time()

#for each element
for i in range(numElements):
    #create a randomValue
    randomValue=random.uniform(0,numElements)

    if i%100000==0: print(" now at "+str(i))

    # we insert in the list, the first element is always the iteration number and the second one is the random number generated
    # Values larger than numElements/2. are added to the end of the list, the smaller ones are added to the beginning of the list
    if randomValue>numElements/2.:
        largeList.append((i,randomValue))
    else:
        largeList.insert(0,(i,randomValue))

    # Also add to the dictionary, the iteration is the key and the randomValue is the Value
    largeDict[i]=randomValue
end = time.time()

print("finished data generation in (TIME 1) "+str(end - start))
#print "Dictionary: "+str(largeDict)
#print "List"+str(largeList)


#now search for an element in the list and in the dictionary
randomSearchKey=int(random.uniform(0,numElements))

print("searching for key "+str(randomSearchKey))
print("In the list ")
start = time.time()
found=False
i=0
while not found and i<len(largeList):
    if largeList[i][0]==randomSearchKey:
        found=True
        value=largeList[i][1]
    else:
        i=i+1
end = time.time()
print("found key in the list in (TIME 2) "+str(end - start)+" with value "+str(value))


print("searching for key "+str(randomSearchKey))
print("In the dictionary ")
start = time.time()
value= largeDict[randomSearchKey]
end = time.time()

print("found key in the dictionary in (TIME 3) "+str(end - start)+" with value "+str(value))


print("\n\n\n\n\n\n Dictionary example 3 (see reference), sorting a dictionary")
