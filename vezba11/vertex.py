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
    for cvor in Graph:
        n=0
        for edge in Edges:
            if edge.second==cvor:
                n+=1
        Lista.append(n)
    return Lista

def GetOutDegrees(Graph,Edges):
    Lista=[]
    for cvor in  Graph:
        n=0
        for edge in Edges:
            if edge.first==cvor:
                n+=1
        Lista.append(n)
    return Lista

def find_edge_value(Edges, u, v):
    for x in Edges:
        if x.first == u and x.second == v:
            return x.value
    return inf

def initialize_single_source(G, s):
    for v in G:
        v.d = inf
        v.p = None
    s.d = 0

def relax(u, v, w):
    if v.d > u.d + find_edge_value(w, u, v):
        v.d = u.d + find_edge_value(w, u, v)
        v.p = u

def bellman_ford(Graph, Edges, s):
    initialize_single_source(Graph, s)
    for i in range(len(Graph)):
        for edge in Edges:
            relax(edge.first, edge.second, Edges)
    for edge in Edges:
        if edge.first.d > edge.second.d + find_edge_value(Edges, edge.first, edge.second):
            return False
    return True

def create_path(G, s, v, L):
    if v == s:
        L.append(v)
    elif v.p == None:
        return None
    else:
        create_path(G, s, v.p, L)
        L.append(v)
    return L

def ShortestPath(G, nodeA, nodeB, w):
    bellman_ford(G, w, nodeA)
    L = []
    L = create_path(G, nodeA, nodeB, L)
    n = G[len(G) - 1].d
    return (L, n)

def UpdateEdge(Edges,nodeA,nodeB,weight):
    if find_edge_value(Edges,nodeA,nodeB) != inf:
        for edges in Edges:
            if edges.first==nodeA and edges.second== nodeB:
                edges.val=weight
    else:
        Edges.append(Edge(nodeA,nodeB,weight))
