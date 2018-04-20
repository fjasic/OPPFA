import sys
from node import Data,Node
from tree import Tree
import random

def randomList(min,max,elements):
    list=random.sample(range(min,max),elements)
    return list

if __name__=="__main__":
    lista=randomList(0,10,10)
    print(lista)
    t=Tree()
    for i in lista:
        d=Data(i,str(i))
        z=Node(d)
        t.treeInsert(z)

    print("---TESTIRANJE---")
    print("----IN ORDER TREE WALK TEST----")
    t.inorderTreeWalk()