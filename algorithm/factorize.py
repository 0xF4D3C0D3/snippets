import itertools

def factorize(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1: return
        while n%i == 0:
            n /= i
            yield i
