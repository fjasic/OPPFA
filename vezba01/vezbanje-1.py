import time
import calendar
localtime=time.asctime(time.localtime(time.time()))
print ("current time :" ,localtime )

cal=calendar.month(2018,3)
print("calendar for march: ",cal)

clock=time.clock()
print("clock of cpu: " ,clock)


def printtime(str):
    print(str)
    return

printtime("balablalbaba")

def printlist(myList):
    myList.append([1,2,3,4])
    print("values inside function: ",myList)
    return
def printlist1(myList):
    myList=[1,2,3,4]
    print("values inside function: ",myList)
    return

myList=[100,140,130]
printlist(myList)
print("values outside the function: ",myList)
printlist1(myList)
print("values outside the function: ",myList)

def printinfo(*vartuple):
    print("output is :")
   # print(arg1)
    for var in vartuple:
        print (var)
    return

printinfo(10)
printinfo(100,101,102)
