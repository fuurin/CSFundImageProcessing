import random
import time
import sys
import itertools

def createRandomIntList(numInts,xMin=-50,xMax=50):
    listOfInts=[]

    for i in range(numInts):
        listOfInts.append(random.randint(xMin,xMax))

    return listOfInts        

def factorial(n):
    if n==1: return 1
    else: return n*factorial(n-1)
        

def sumNFirstNumbers(n):
    if n==1: return 1
    else: return n+sumNFirstNumbers(n-1)


def fibonacci(n):
    if n==0: return 0
    elif n==1: return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def printFunc(x):
    if(x<1):return ""
    else:
        output=str(x)+printFunc(x-1)
        print output
        return ""
    
if __name__=="__main__":

    n=1000
    
    print "Data size here is : "+str(n)

   # printFunc(n)
    
    #print sumNFirstNumbers(n)
    
    start = time.time()
    f=factorial(n)
    end = time.time()
    print "finished computing factorial of "+str(n)+", "+str(f)+" with O(n!) complexity in (TIME 1) "+str(end - start)

    start = time.time()
    result=fibonacci(n)
    end = time.time()
    print "finished computing the "+str(n)+"th fibonacci number "+str(result)+" with exponential O(2 to the n) complexity in (TIME 2) "+str(end - start)



