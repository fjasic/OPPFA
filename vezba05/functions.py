def inorderTreeWalk(x):
    if x!=None:
        inorderTreeWalk(x.left)
        print(x.data.a2)
        inorderTreeWalk(x.right)



def inorderTreeWalkList(x, l):
    if x != None:
        inorderTreeWalkList(x.left, l)
        l.append(x.data)
        inorderTreeWalkList(x.right, l)

def treeSearch(x,k):
    if x==None or k==x.key:
        return x
    if k<k.key:
        return treeSearch(x.left,k)
    else:
        return treeSearch(x.right,k)

def iterativeTreeSearch(x,k):
    while x!=None and k!=x.key:
        if k<x.key:
            x=x.left
        else:
            x=x.right
    return x

def treeMinimum(x):
    while x.left!=None :
        x=x.left
    return x

def treeMaximum(x):
    while x.right!=None:
        x=x.right
    return x

def treeSuccssor(x):
    if x.right!=None:
        return treeMinimum(x.right)
    y=x.p
    while y!=None and x == y.right:
        x=y
        y=y.p
    return y

def treeInsert(T,z):
    y = None
    x = T
    while x != None:
        y = x
        if z.data.a1 < x.data.a1:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T = z
    elif z.data.a1 < y.data.a1:
        y.left = z
    else:
        y.right = z
    return T


def transplant(T, u, v):
    if u.p==None:
        T.root =v
    else:
        if u==u.p.left:
            u.p.left=v
        else:
            u.p.right=v
    if v!=None:
        v.p=u.p

def treeDelete(T,z):
    if z.left==None:
        transplant(T,z,z.right)
    else:
        if z.right==None:
            transplant(T,z,z.left)
        else:
            y = treeMinimum(z.right)
            if y.p != z:
                transplant(treeDelete, y, y.right)
                y.right = z.right
                y.right.p = y
            transplant(T, z, y)
            y.left = z.left
    y.left.p = y






