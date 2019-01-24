import random
import time
import sys
import itertools

def createRandomIntList(numInts,xMin=-50,xMax=50):
    listOfInts=[]

    for i in range(numInts):
        listOfInts.append(random.randint(xMin,xMax))

    return listOfInts        

def countOccurrences(l,e):
    returnValue=0
    for x in l:
        if(x==e):returnValue+=1
    return returnValue

def permutations(n):
    permutationsList=[]
    #create list with all possible elements
    for i in range(n):
        permutationsList.append(i)
    aa=list(itertools.permutations(permutationsList))
    #print aa

if __name__=="__main__":

    n=75000

    print "Data size here is : "+str(n)

    #O(n), create a list
    start = time.time()
    myList=createRandomIntList(n)
    end = time.time()
    print "finished data generation with Linear ( O(n) )  complexity in (TIME 1) "+str(end - start)
    #print myList

    #O(1)
    start = time.time()
    randomIndex=random.randint(0,n-1)
    randomListValue=myList[randomIndex]
    end = time.time()
    print "finished accessing random data with constant O(1) complexity in (TIME 2) "+str(end - start)


    #O(n*n)
    start = time.time()
    repetitions=[0]*n
    i=0
    for x in myList:
        repetitions[i]=countOccurrences(myList,x)
        i=i+1
    end = time.time()
    print "finished counting occurrences in list with quadratic O(n*n) complexity in (TIME 3) "+str(end - start)

    #O(nlog n)
    start = time.time()
    myList.sort()
    end = time.time()
    print "finished sorting a list with n elements with O(n log n) complexity in (TIME 4) "+str(end - start)

    # Careful! DO NOT MAKE THIS BIG very fast, it eats up memory very fast
    newN=10
    #O(2 to the n)
    start = time.time()
    permutations(newN)
    end = time.time()
    print "finished computing the permutations of "+str(newN)+" with exponential O(2 to the n) complexity in (TIME 5) "+str(end - start)

