from math import inf
from random import randint

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Vertex:
    def __init__(self, val):
        self.val = val
        self.con = []

    def print_neighbours(self):
        print([i.val for i in self.con])

    def add_neighbour(self, neighbour):
        self.con.append(neighbour)

def find_edge_value(w, u, v):
    for x in w:
        if x.source == u and x.destination == v:
            return x.weight
    return inf

def print_path(G, s, v):
    if v == s:
        print(s.val, end =" " + "->")
    elif v.p == None:
        print ("nema putanje od", s.val, "do", v.val)
    else:
        print_path(G, s, v.p)
        print(v.val, end = " "+ "->")


def generate_graph(n, m, edge):
    N = n
    G = []
    for i in range(N):
        G.append(Vertex(i))

    w = []
    for i in range(N):
        for j in range(randint(1, m)):
            r = i
            while r == i:
                r = randint(0, N - 1)
            w.append(Edge(G[i], G[r], randint(0, edge)))
    return (G, w)

def print_graph(G, w):
    for v in G:
        print("za cvor:", v.val+1)
        for edge in w:
            if edge.source == v:
                print("Ivica:", edge.destination.val, "Cena:", edge.weight)
        print()

def relax(u, v, w):
    if v.d > u.d + find_edge_value(w, u, v):
        v.d = u.d + find_edge_value(w, u, v)
        v.p = u

def initialize_single_source(G, s):
    for v in G:
        v.d = inf
        v.p = None
    s.d = 0

def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = []
    Q = G[:]
    while Q:
        u = extract_min(Q)
        S.append(u)
        for v in G:
            relax(u, v, w)

def extract_min(G):
    m = G[0] #prvi u listi
    for v in G:
        if v.d < m.d:
            m = v
    G.remove(m)
    return m


if __name__=="__main__":
    s=Vertex("s")
    t=Vertex("t")
    y=Vertex("y")
    x=Vertex("x")
    z=Vertex("z")

    G=[s,t,z,x,y]
    w=[]

    w.append(Edge(s,y,5))
    w.append(Edge(s,t,10))

    w.append(Edge(y,t,3))
    w.append(Edge(y,z,2))
    w.append(Edge(y,x,9))

    w.append(Edge(t,x,1))
    w.append(Edge(t,y,2))

    w.append(Edge(z,x,6))
    w.append(Edge(z,s,7))

    w.append(Edge(x,z,4))

    dijkstra(G,w,s)

    for v in G:
        print("putanja",s.val,"->",v.val,":")
        print_path(G,s,v)
        print(v.d)

    print("-----------------------")
    print("random generisani graph")
    (G,w)=generate_graph(5,5,10)
    s=G[0]

    print_graph(G,w)

    dijkstra(G,w,s)

    for v in G:
        print("putanja", s.val, "->", v.val, ":")
        print_path(G, s, v)
        print("ukupna putanja",v.d)

