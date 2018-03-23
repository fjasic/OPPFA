import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list


###################

#MAX_HEAPIFY


###################

#parent
def parent(i):
    return i//2
#left
def left(i):
    return 2*i +1

#right
def right(i):
    return 2*i+2

def max_heapify(A,i,size):
    l=left(i)
    r=right(i)
    if l<size and A[l]>A[i]:
        largest=l
    else:
        largest=i
    if r<size and A[r]> A[largest]:
        largest=r
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest,size)


def build_max_heap(A):
    size=len(A)
    for i in reversed(range(len(A)-1)):
        max_heapify(A,i,size)

def heapsort(A):
    build_max_heap(A)
    size=len(A)
    for i in reversed(range(1,size)):
        A[0],A[i]=A[i],A[0]
        size = size-1
        max_heapify(A,0,size)

def test_heap_sort(element):
    start_time=time.clock()
    nesortian_niz=random_list(1,element+1,element)
    print("nesortirani niz izgleda ovako :",nesortian_niz)
    heapsort(nesortian_niz)
    print("heap sortiranje,niz izgleda ovako",nesortian_niz)
    end_time=time.clock() - start_time
    print("heap sorting DURATION for "+str(element-1) + " elements is " + str(end_time))


################################

#bucket sort

################################
def random_list1(min, max, elements):
    list1 = [random.choice(range(min, max)) for _ in range(elements)]
    return list1


def index(i):
    return i // 100


def bucket_sort(A):
    size = 10
    B = [0] * (size)
    for i in range(size - 1):
        B[i] = []
    for i in range(len(A)):
        B[index(A[i])].append(A[i])
    for i in range(0, size - 1):
        B[i].sort()
    A.clear()
    for i in range(size - 1):
        A += B[i]



################################
def test_bucket_sort(element):
    start_time=time.clock()
    nesortian_niz=random_list1(0,100,element)
    print("nesortirani niz izgleda ovako :",nesortian_niz)
    bucket_sort(nesortian_niz)
    print("bucket sortiranje,niz izgleda ovako",nesortian_niz)
    end_time=time.clock() - start_time
    print("heap sorting DURATION for "+str(element-1) + " elements is " + str(end_time))

################################
def counting_sort(A,B,k):
    C=[0]*k
    for j in range(len(A)):
        C[A[j]] = C[A[j]] +1
    #u C[i] se sad nalazi broj elemenata jednak i
    for i in range(1, k):
        C[i] = C[i] + C[i -1]
    #u C[i] se sad nalazi broj elemenata manji ili jednak i
    for j in reversed(range(len(A))):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1

def test_counting_sort(elements):
    l=random_list1(1,100,elements)
    r=[0]*len(l)
    k=max(l)+1
    print("nesortirani niz izgleda ovako",l)
    start_time=time.clock()
    counting_sort(l,r,k)

    print("sortirani niz izgleda ovako",r)
    end_time=time.clock()-start_time
    print("DURATION counting sort :",end_time)

if __name__ == "__main__":
    for i in range(1,10000,500):
        test_counting_sort(i)