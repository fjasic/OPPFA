import sys
from vertex import *

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

    #print path
    for v in G:
        print("path",s.val,"->",v.val,":")
        print_path(G,s,v)
        print(v.d)


    print("random generated graph")
    (G,w)=generate_graph(5,5,10)
    s=G[0]

    #print generated graph
    print_graph(G,w)

    #dijkstra
    dijkstra(G,w,s)

    # print path
    for v in G:
        print("path", s.val, "->", v.val, ":")
        print_path(G, s, v)
        print("total distance",v.d)
