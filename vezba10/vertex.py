import sys
from math import inf
from queue import Queue as queue
from random import randint

class Edge:
    def __init__(self, first, second, val):
        self.first = first
        self.second = second
        self.val = val


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
        if x.first == u and x.second == v:
            return x.val
    return inf

def print_path(G, s, v):
    if v == s:
        print(s.val, end = " ")
    elif v.p == None:
        print ("no path found from", s.val, "to", v.val, "exists")
    else:
        print_path(G, s, v.p)
        print(v.val, end = " ")

def initialize_single_source(G, s):
    for v in G:
        v.d = inf
        v.p = None
    s.d = 0

def extract_min(G):
    m = G[0]
    for v in G:
        if v.d < m.d:
            m = v
    G.remove(m)
    return m

def relax(u, v, w):
    if v.d > u.d + find_edge_value(w, u, v):
        v.d = u.d + find_edge_value(w, u, v)
        v.p = u

def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = []
    Q = G[:]
    while Q:
        u = extract_min(Q)
        S.append(u)
        for v in G:
            relax(u, v, w)

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
        print("Node:", v.val)
        for edge in w:
            if edge.first == v:
                print("\tEdge:", edge.second.val, "Distance:", edge.val)
        print()