import random
import time
from math import floor


class Data:
    def __init__(self, key=None):
        self.key = key
        self.literal = str(key)


class ChaindedHash:
    def __init__(self, p=23, n=10000):
        self.p = p
        self.n = n
        self.a = random.randint(1, p)
        self.b = random.randint(0, p)
        self.Lista = [[]] * n

    def insert_hash(self, x):
        h = self.hash1(x.key)
        if x in self.Lista[h]:
            self.Lista[h].remove(x)
        self.Lista[h].append(x)

    def search_hash(self, k):
        h = self.hash1(k)
        for i in self.Lista[h]:
            if i.key == k:
                return i
            return None

    def hash_delete(self, x):
        h = self.hash1(x.key)
        if x in self.Lista[h]:
            self.Lista[h].remove(x)

    def hash(self, k):
        return k % m

    def hash1(self, k):
        return self.hash3(k)

    def hash2(self, k):
        KNUTH = 0.6180339887
        return floor(m * ((k * KNUTH) % 1))

    def hash3(self, k):
        return ((self.a * k + self.b) % p) % m


def random_list(min, max, N):
    list = random.sample(range(min, max), N)
    return list


def test(n, p, m):
    lista_random = random_list(1, n + 1, n)
    start_time = time.clock()

    L = ChaindedHash(p, m)
    for i in lista_random:
        x = Data(i)
        L.insert_hash(x)

    end_time = time.clock()
    print("duration:", (end_time - start_time), " n: ", n, " p: ", p, " m: ", m)


if __name__ == "__main__":
    for n in [500,10000, 50000, 100000]:
        for p in [23, 9973, 99991]:
            for m in [p, p // 2, p // 4]:
                test(n, p, m)
