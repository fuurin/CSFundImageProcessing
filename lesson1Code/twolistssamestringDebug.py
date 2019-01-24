import listFileIO as IO

def listContainsString(myList,myString):
    #Complete code here, return True if myString appears in myList
    #print("Inside listContainsString, looking for \n "+myString+" in \n"+str(myList))
    return myString in myList

def listsShareString(list1,list2):
    i=0
    found=False
    while found==False and (i<len(list1)):
        listContainsString(list2,list1)
        if(found==True):
            return True
        else:
            i=i+1

if __name__=="__main__":

    # reads a list of Strings from the file indicated by the name
    list1=IO.readStringListFromFile("input4.txt")
    # reads a list of Strings from the file indicated by the name
    list2=IO.readStringListFromFile("input3.txt")

    print("First List:"+str(list1))
    print("Second List:"+str(list2))

    print("OUTPUT: "+str(listsShareString(list1,list2)))
