import sys
from math import inf
from queue import Queue as queue

global time

class Vertex:
    def __init__(self, val):
        self.val = val
        self.con = []

    def print_neighbours(self):
        print([i.val for i in self.con])

    def add_neighbour(self, neighbour):
        self.con.append(neighbour)

class VertexColor:
    BLACK = 0
    GRAY = 127
    WHITE = 255

def bfs(G, s):
    for u in G:
        u.color = VertexColor.WHITE
        u.d = inf
        u.p = None
    s.color = VertexColor.GRAY
    s.d = 0
    s.p = None
    Q = queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in u.con:
            if v.color == VertexColor.WHITE:
                v.color = VertexColor.GRAY
                v.d = u.d + 1
                v.p = u
                Q.put(v)
        u.color = VertexColor.BLACK

def print_path(G, s, v):
    if v == s:
        print(s.val, end = " ")
    elif v.p == None:
        print ("no path found from", s.val, "to", v.val, "exists")
    else:
        print_path(G, s, v.p)
        print(v.val, end = " ")

def dfs(G):
    global time
    for u in G:
        u.color = VertexColor.WHITE
        u.p = None
    time = 0
    for u in G:
        if u.color == VertexColor.WHITE:
            dfs_visit(G, u)

def dfs_visit(G, u):
    global time
    time += 1
    u.d = time
    u.color = VertexColor.GRAY

    for v in u.con:
        if v.color == VertexColor.WHITE:
            v.p = u
            dfs_visit(G, v)
    u.color = VertexColor.BLACK
    time += 1
    u.f = time

def topological_sort(G):
    dfs(G)
    L = sorted(G, key=lambda x: x.f, reverse=True)
    return L