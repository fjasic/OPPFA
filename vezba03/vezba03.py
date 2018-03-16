import random
import time
from math import inf


def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

#MERGE SORT
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [], []
    i, j = 0, 0
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(inf)
    R.append(inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


#QUICK SORT
def partition(A,p,r):
    x=A[r]
    i=p
    for j in range(p,r):
        if A[j] <= x:
            A[i],A[j]=A[j],A[i]
            i=i+1
    A[i],A[r]=A[r],A[i]
    return i

def randomized_partition(A,p,r):
    i=random.randint(p,r)
    A[r],A[i]=A[i],A[r]

    return partition(A,p,r)

def randomized_quicksort(A,p,r):
    if p<r:
        q=randomized_partition(A,p,r)
        randomized_quicksort(A,p,q-1)
        randomized_quicksort(A,q+1,r)
        return A

def test_merge(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()

    sortirano=merge_sort(l, 0, len(l) - 1)

    end_time = time.clock() - start_time
    print("Elementi MERGE_SORT:", elements)
    print("sortirana lista je :",sortirano)
    print("Duration: ", end_time)


def test_quick(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()

    sortirano=randomized_quicksort(l,0,len(l)-1)

    end_time = time.clock() - start_time
    print("Elementi QUICK_SORT:", elements)
    print("soritarana lista quick sort :",sortirano)
    print("Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 10000, 500):
        test_quick(i)