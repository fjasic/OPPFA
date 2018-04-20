from functions import *

class Tree(object):

    def __init__(self,r=None):
        self.root=r

    def inorderTreeWalk(self):
        return inorderTreeWalk(self.root)
    def treeSearch(self,k):
        return treeSearch(self.root,k)
    def iterativeTreeSearch(self,k):
        return iterativeTreeSearch(self.root,k)
    def treeMinimum(self):
        return treeMinimum(self.root)
    def treeMaximum(self):
        return treeMinimum(self.root)
    def treeSuccessor(self,x):
        treeSuccssor(x)
    def treeInsert(self,z):
        self.root= treeInsert(self.root,z)
    def transplant(self,u,v):
        return transplant(self.root,u,v)
    def treeDelete(self,z):
        return treeInsert(self.root,z)
    def inorderTreeWalkList(self, l):
        inorderTreeWalkList(self.root, l)