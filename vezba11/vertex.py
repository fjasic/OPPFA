from math import inf

class Edge:
    def __init__(self,first,second,value):
        self.first=first
        self.second=second
        self.value=value

class Vertex:
    def __init__(self,val):
        self.val=val
        self.con=[]

def MakeGraph():
    a=Vertex("a")
    b=Vertex("b")
    c=Vertex("c")
    d=Vertex("d")
    e=Vertex("e")
    f=Vertex("f")
    g=Vertex("g")

    graph=[a,b,c,d,e,f,g]

    edges=[]
    edges.append(Edge(a,b,8))
    edges.append(Edge(a,c,6))
    edges.append(Edge(b,d,10))
    edges.append(Edge(c,d,15))
    edges.append(Edge(c,e,9))
    edges.append(Edge(d,e,14))
    edges.append(Edge(d,f,4))
    edges.append(Edge(e,f,13))
    edges.append(Edge(e,g,17))
    edges.append(Edge(f,g,7))

    return (graph,edges)

def GetInDegrees(Graph,Edges):
    Lista=[]
    for vertex in Graph:
        n=0
        for edge in Edges:
            if edge.second==vertex:
                n+=1
        Lista.append(n)
    return Lista

def GetOutDegrees(Graph,Edges):
    Lista=[]
    for vertex in Graph:
        n=0
        for edge in Edges:
            if edge.first==vertex:
                n+=1
        Lista.append(n)
    return Lista

def find_edge_value(Edges, source, destination):
    for x in Edges:
        if x.first == source and x.second == destination:
            return x.value
    return inf

def initialize_single_source(Graph, source):
    for vertex in Graph:
        vertex.estimate = inf
        vertex.predecessor = None
    source.estimate = 0

def relax(source, destination, weight):
    if destination.estimate > source.estimate + find_edge_value(weight, source, destination):
        destination.estimate = source.estimate + find_edge_value(weight, source, destination)
        destination.predecessor = source

def bellman_ford(Graph, Edges, s):
    initialize_single_source(Graph, s)
    for i in range(len(Graph)):
        for edge in Edges:
            relax(edge.first, edge.second, Edges)
    for edge in Edges:
        if edge.first.estimate > edge.second.estimate + find_edge_value(Edges, edge.first, edge.second):
            return False
    return True

def create_path(Graph, source, destination, Lista):
    if destination == source:
        Lista.append(destination)
    elif destination.predecessor == None:
        return None
    else:
        create_path(Graph, source, destination.predecessor, Lista)
        Lista.append(destination)
    return Lista

def ShortestPath(Graph, nodeA, nodeB, Edges):
    bellman_ford(Graph, Edges, nodeA)
    L = []
    L = create_path(Graph, nodeA, nodeB, L)
    n = Graph[len(Graph) - 1].estimate
    return (L, n)

def UpdateEdge(Edges,nodeA,nodeB,weight):
    if find_edge_value(Edges,nodeA,nodeB) != inf:
        for edges in Edges:
            if edges.first==nodeA and edges.second== nodeB:
                edges.value=weight
    else:
        Edges.append(Edge(nodeA,nodeB,weight))
