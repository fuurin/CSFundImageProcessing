import random
import time
import sys
import string

def createRandomIntList(numInts,xMin=-50,xMax=50):
    listOfInts=[]

    for i in range(numInts):
        listOfInts.append(random.randint(xMin,xMax))

    return listOfInts

#Reference: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def createRandomStringList(numStrings,maxLength=20):
    listOfStrings=[]

    for i in range(numStrings):
        length=random.randint(1,maxLength)
        listOfStrings.append(string_generator(length))

    return listOfStrings


if __name__=="__main__":

    n=100

    print("n is now "+str(n))

    #O(n), create a lint
    start = time.time()
    myList=createRandomIntList(n)
    #myList=createRandomStringList(n,10)
    #myList=["hollow","hey","ashroa",12,"power","mochi"]
    end = time.time()
    print(myList)

    #copy the list as many times as needed
    myOtherList=list(myList)
    myThirdList=list(myList)
    myFourthList=list(myList)

    #O(n*logn)
    start = time.time()
    myList.sort()
    end = time.time()
    time1=end - start
    print("finished sorting list with O(n*logn) timsort "+str(time1))
    print(myList)

    print(str(n)+" "+str(time1))
