import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

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

#--BUBBLE SORT--
def bubble_sort(a):
    for lista_duzina in range(len(a)-1,0,-1):
        for j in range(lista_duzina):
            if(a[j+1]<a[j]):
                kljuc=a[j]
                a[j]=a[j+1]
                a[j+1]=kljuc
    return a



#--LINEARNA PRETRAGA--
def linearna_pretraga(a,trazena_vrednost):
    for i in range(len(a)):
        if trazena_vrednost==a[i]:
            print("trazena vrednost je:  " + str(trazena_vrednost) + " i nalazi se na poziciji: " + str(i+1) )

#BINARNA PRETRAGA
def binarna_pretraga(a, trazena_vrednost):
    minimum = 0
    maximum = len(a)
    def rekurzija(minimum, maximum):
            m = int((minimum + maximum) / 2)
            if a[m] < trazena_vrednost:
                return rekurzija(m + 1, maximum)
            elif a[m] > trazena_vrednost:
                return rekurzija(minimum, m - 1)
            else:
                return m
    print("trazeni index je " + str(rekurzija(0, len(a) -1)))

def test_binarna_pretraga():
    nesortirana_lista=random_list(10,100,20)

    print("nesortirana lista izgleda ovako",nesortirana_lista)
    sortirana_lista=insertion_sort(nesortirana_lista)
    print("sortirana insertion sort lista izgleda: ", (sortirana_lista))

    trazena_vrednost=int(input("unesi vrednost koju hoces da nadjes: "))
    start_time=time.clock()
    binarna_pretraga(sortirana_lista,trazena_vrednost)
    end_time = time.clock() - start_time
    print("Duration: ", end_time)

if __name__ == "__main__":
    test_binarna_pretraga()