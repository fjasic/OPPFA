import random
import time


class Data:
    def __init__(self, key=None):
        self.key = key
        self.literal = str(key)


class HashTable:
    def __init__(self, m=100000, c1=1 / 2, c2=1 / 2):
        self.m = m
        self.c1 = c1
        self.c2 = c2
        self.T = [None] * m

    def hash_insert(self, k):
        i = 0
        while True:
            j = self.hash(k, i)
            if self.T[j] == None:
                self.T[j] ==k
                return j
            else:
                i = i + 1
            if i == self.m:
                break
        print("ERROR hash table overflow")

    def hash_search(self, k):
        i = 0
        while True:
            j = self.hash(k, i)
            if self.T[j] == None:
                return j
            i = i + 1
            if self.T[j] == None or i == self.m:
                break
        return None

    def hash_delete(self, x):
        h = self.hash1(x.key)
        if x in self.T[h]:
            self.T[h].remove(x)

    def hash(self, k, i):
        return self.hash1(k, i)

    def hash1(self, k, i):
        return (self.h1(k) + i) % self.m

    def h1(self, k):
        return k % self.m

    def h2(self, k):
        return 1 + (k % (self.m - 1))

    def hash2(self, k, i):
        return (self.h1(k) + self.c1 * i + self.c2 * i ** 2) % self.m

    def hash3(self, k, i):
        return (self.h1(k) + self.h2(k)) % self.m

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list


def test(n, m):
    l = random_list(1, n + 1, n)
    start_time = time.clock()

    L = HashTable(m)

    for i in l:
        L.hash_insert(i)

    end_time = time.clock() - start_time

    print("n:", n, "m:", m, "duration:", end_time)


if __name__ == "__main__":
    for n in [10000, 50000, 100000]:
        for m in [n, n // 2, n // 4]:
            test(n, m)
