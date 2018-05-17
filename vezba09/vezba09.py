import sys
from vertex import *

if __name__ == "__main__":
    print("\n===G1===")
    # Create graph 1
    G1 = []
    for i in range(5):
        g = Vertex(i + 1)
        G1.append(g)

    # Connect graph 1
    G1[0].add_neighbour(G1[1])
    G1[0].add_neighbour(G1[4])

    G1[1].add_neighbour(G1[0])
    G1[1].add_neighbour(G1[4])
    G1[1].add_neighbour(G1[2])
    G1[1].add_neighbour(G1[3])

    G1[2].add_neighbour(G1[1])
    G1[2].add_neighbour(G1[3])

    G1[3].add_neighbour(G1[1])
    G1[3].add_neighbour(G1[4])
    G1[3].add_neighbour(G1[2])

    G1[4].add_neighbour(G1[3])
    G1[4].add_neighbour(G1[0])
    G1[4].add_neighbour(G1[1])

    print("neighbours of node 4:")
    G1[3].print_neighbours()

    print("path from 4 to 1:")
    bfs(G1,G1[3])
    print_path(G1,G1[3],G1[0])

    print("\n==G2==")
    #create nodes
    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    belt = Vertex("belt")
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    socks = Vertex("socks")
    shoes = Vertex("shoes")
    watch = Vertex("watch")

    undershorts.con=[pants,belt]
    pants.con=[belt,shoes]
    belt.con=[jacket]
    shirt.con=[tie,belt]
    tie.con=[jacket]
    jacket.con=[]
    socks.con=[shoes]
    shoes.con = []
    watch.con = []
    #create graph 2
    G2 = [shirt, undershorts, pants, belt, tie, jacket, socks, shoes, watch]

    # Topological sort
    L = topological_sort(G2)
    print([(i.val, i.d, i.f) for i in reversed(L)])




