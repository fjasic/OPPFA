from vertex import *

if __name__ =="__main__":
    #zadatak1
    print("\n ZADATAK 1 : MakeGraph() ")
    (Graph,Edges)=MakeGraph()
    print([x.val for x in Graph])
    print([(x.first.val,x.second.val,x.value) for x in Edges])

    print("\n ZADATAK 2 : GetInDegrees() & GetOutDegrees() ")
    ListaInDegrees=GetInDegrees(Graph,Edges)
    ListaOutDegrees=GetOutDegrees(Graph,Edges)

    print("in degrees:",[x for x in ListaInDegrees])
    print("in degrees:",[x for x in ListaOutDegrees])

    for i in range(len(Graph)):
        print("Node",Graph[i].val,"In degrees: ",ListaInDegrees[i],"Out degrees",ListaOutDegrees[i])

    print("\n ZADATAK 3 : ShortestPath()")
    bellman_ford(Graph,Edges,Graph[0])
    (Lista,putanja)=ShortestPath(Graph,Graph[0],Graph[6],Edges)

    print("Shortest path from",Graph[0].val,"to",Graph[6].val,"is",putanja)
    print("PATH: ")
    for i in range(len(Lista)):
        print("|")
        print(Lista[i].val)
    print()

    print("\n ZADATAK 4 : UpdateEdge()")
    UpdateEdge(Edges,Graph[0],Graph[3],15)
    print([(x.first.val,x.second.val,x.value) for x in Edges])

    print("\n ZADATAK 5 :NewShortestPath() ")
    UpdateEdge(Edges,Graph[1],Graph[2],-4)
    print([(x.first.val,x.second.val,x.value) for x in Edges])

    bellman_ford(Graph, Edges, Graph[0])
    (Lista, putanja) = ShortestPath(Graph, Graph[0], Graph[6], Edges)

    print("NEW Shortest path from", Graph[0].val, "to", Graph[6].val, "is", putanja)
    print("PATH: ")
    for i in range(len(Lista)):
        print("|")
        print(Lista[i].val)
    print()