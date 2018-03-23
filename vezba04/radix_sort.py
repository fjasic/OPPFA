# Python program for implementation of Radix Sort
import random
import time


def random_list(minimum, maximum, elements):
    lista = random.sample(range(minimum, maximum), elements)
    return lista


# radim counting sort za cifre
# i prosledjenim exponentonentom
def countingSort(A, exponentonent):
    n = len(A)
    # u output smestam sortiran niz
    output = [0] * n

    count = [0] * 10

    # koliko se broj ponavlja smestam u counter
    for i in range(0, n):
        index = (A[i] / exponentonent)
        count[int((index) % 10)] += 1

    # counter sada sadrzi poziciju broja u outputuy
    for i in range(1, 10):
        count[i] += count[i - 1]

    # pravim output
    i = n - 1
    while i >= 0:
        index = (A[i] / exponentonent)
        output[count[int((index) % 10)] - 1] = A[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # vracam output nazad u A tako da sad imam sortiran niz
    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]

# radix sort
def radixSort(A):
    # nalazim najveci broj
    max1 = max(A)

    # radim counting sort za svaku cifru
    # i prosledjujem exponent
    exponent = 1
    while max1 / exponent > 0:
        countingSort(A, exponent)
        exponent *= 10

# testiranje
def test_radix_sort(elements):
    lista = random_list(0, elements + 1, elements)
    print("nesortirana lista izgleda ovako", lista)
    start_time = time.clock()
    radixSort(lista)
    print("radix sortirana lista izgleda ovako", lista)
    end_time = time.clock() - start_time
    print("Duration for radix_sort: ", end_time)
    print("Number of elements",elements)
    print("-------------------------------------------------------------------")

if __name__ == "__main__":
    for i in range(1, 10000, 500):
        test_radix_sort(i)
