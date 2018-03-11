import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

start_time = time.clock()

#--INSERTION_SORT--
def insertion_sort(a):
    for j in range(1,len(a)):
        kljuc=a[j]
        i=j-1
        while (i>=0 and a[i]>kljuc):
            a[i+1]=a[i]
            i=i-1
        a[i+1]=kljuc
    return a

#lista=random_list(10,110,20)

#insertion_sort(lista)
#print("insertion sort lista izgleda: ", lista)

"""
#--BUBBLE SORT--
def bubble_sort(a):
    for lista_duzina in range(len(a)-1,0,-1):
        for j in range(lista_duzina):
            if(a[j+1]<a[j]):
                kljuc=a[j]
                a[j]=a[j+1]
                a[j+1]=kljuc
    return a
lista=random_list(10,100,20)
bubble_sort(lista)
print("bubble sort lista izgleda",lista)
"""

"""
#--LINEARNA PRETRAGA--
def linearna_pretraga(a,trazena_vrednost):
    for i in range(len(a)):
        if trazena_vrednost==a[i]:
            print("trazena vrednost je:  " + str(trazena_vrednost) + " i nalazi se na poziciji: " + str(i+1) )


lista=random_list(10,100,20)
print("lista izgleda ovako :",lista)
trazena_vrednost=int(input("unesi vrednost koju hoces da nadjes: "))
linearna_pretraga(lista,trazena_vrednost)
"""

#BINARNA PRETRAGA
def binarna_pretraga(a, trazena_vrednost):
    min = 0
    max = len(a)
    def rekurzija(min, max):
            m = int((min + max) / 2)
            if a[m] < trazena_vrednost:
                return rekurzija(m + 1, max)
            elif a[m] > trazena_vrednost:
                return rekurzija(min, m - 1)
            else:
                return m

    print("trazeni index je " + str(rekurzija(0, len(a) -1)))


sortirana_lista=insertion_sort(random_list(10,100,20))
print("insertion sort lista izgleda: ", (sortirana_lista))

trazena_vrednost=int(input("unesi vrednost koju hoces da nadjes: "))
binarna_pretraga(sortirana_lista,trazena_vrednost)



end_time = time.clock() - start_time
print("Duration: ", end_time)
