from enum import Enum	
import math
import heapq


class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None,id = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.id = id

    #def __lit__(self,vertex):
       # return setlf.data < vertex.data)


class Edge:
    def __init__(self,source = None, destination = None, weight = None) :
        self.source = source
        self.destination = destination
        self.weight = weight
        
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		
def printLista(lista):
     for i in range (0,len(lista)):
        
        print("\n")
        
        for j in range (0,len(lista[i])):
            #print("->",lista[i][j].id)
            print(lista[i][j].id)

def printLista2(lista):
     for i in range (0,len(lista)):
        
        print("\n")
        
        for j in range (0,len(lista[i])):
            #print("->",lista[i][j].id)
            print(lista[i][j].source, " ->",lista[i][j].destination)
         

def initialize_single_source(G, s):
    for vertex in G:
        vertex.d2 = math.inf
        vertex.p = None
    s.d2 = 0

def relax(u, v, w):
    if v.d2 > (u.d2 + w(u, v)):
        v.d2 = u.d2 + w(u, v)
        v.p = u


def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = list()
    Q = heapq.heapify(G)
    while Q != []:
        u = heapq.heappop(G)
        S.append(u)
        for edge in u.edges:
            relax(u,v, w)
        
    
    

if __name__ == "__main__":
		
    u1 = Vertex(c=VertexColor.GRAY, d1 = 11, d2=22, id = 1,)
    u2 = Vertex(c=VertexColor.WHITE,  d1=33, d2=4, id = 2)
    u3 = Vertex(c=VertexColor.WHITE, d1=1, d2=22, id = 3)
    u4 = Vertex(c=VertexColor.WHITE,  d1=33, d2=4, id = 4)
    u5 = Vertex(c=VertexColor.WHITE, d1=1, d2=22, id = 5)

    e1 = Edge(source = 1 ,destination = 2 ,weight = 10)
    e2 = Edge(source = 2 ,destination = 4,weight = 1)
    e3 = Edge(source = 2, destination = 3,weight = 2)
    e4 = Edge(source = 3,destination = 2 ,weight = 3)
    e5 = Edge(source = 1,destination = 3, weight = 5)
    e6 = Edge(source = 5,destination = 1 ,weight = 7)
    e7 = Edge(source = 3,destination = 4, weight = 9)
    e8 = Edge(source = 4,destination = 5, weight = 4)
    e9 = Edge(source = 5,destination = 4, weight = 6)
    e10 = Edge(source = 3,destination = 5, weight = 2)

    lista1 = list()
    lista2 = list()
    

    lista2.append([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10])


    lista1.append([u1,u2,u3])
    lista1.append([u2,u3,u4])
    lista1.append([u3,u2,u4,u5])
    lista1.append([u4,u5])
    lista1.append([u5,u4,u1])

    print("Lista cvorova:\n")
    printLista(lista1)

    print("Lista ivica:\n")
    printLista2(lista2)



