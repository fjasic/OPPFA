import sys
from math import inf
class histogram:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
class node:
    def __init__(self,freq):
        self.freq=freq
        self.left=None #prazni desni i levi cvor
        self.right=None

def GetHistogram(Lista):
    d=[]
    res=[]
    for i in Lista:
        if not i in d:  #da li sam ubacio element
            d.append(i) #ako nisam ubacujem ga
    for i in d:
        a=histogram(i,Lista.count(i))   #koliko puta se ponavlja
        res.append(a)
    return  res

def removeElement(element,Lista):
    Lista.remove(element)

def putElement(element,Lista):
    Lista.append(element)

def makeNewElement(element1,element2):
    n=node(element1.freq + element2.freq)#sabiram frekvenciju poljavljivanja i dobijam novi cvor
    n.left=element1
    n.right=element2
    element1.par=n #roditelj je n
    element2.par=n
    return n

def getMinFreq(Lista):
    m=histogram('\0',inf)
    for i in Lista:
        if i.freq < m.freq:
            m=i
    return m

def getEncVal(symbol,Lista):
    res="" #kod
    while not symbol in Lista:
        if symbol.par.left==symbol:
            res+='0' #kad ide u levo onda nulu pisem
        elif symbol.par.right==symbol:
            res+='1'#kad ide u desno onda jedinicu pisem
        symbol=symbol.par
    return res[::-1] #koliko bitova mogu ispisati

def test(s):
    print(s)
    Lista=GetHistogram(s)
    C=Lista[:]
    while len(Lista)>1:
        m1=getMinFreq(Lista)
        removeElement(m1,Lista)
        m2 = getMinFreq(Lista)
        removeElement(m2, Lista)
        m=makeNewElement(m1,m2)
        putElement(m,Lista)
    for symbol in C:
        print("symbol:"+symbol.value,"|kod: "+getEncVal(symbol,Lista),"|frekvencija:"+ str(symbol.freq))


if __name__=="__main__":
    snippets=[['a', 'b'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd'], ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']]
    for s in snippets:
        test(s)