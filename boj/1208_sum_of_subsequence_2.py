from collections import Counter
import itertools


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def how_many_subsequences_that_sum_is(S, A):
    m = len(A)//2
    L, R = A[:m], A[m:]
    c = Counter(sum(s) for s in powerset(L))
    return sum(c[S-sum(s)] for s in powerset(R))

_, S = map(int, input().split())
A = list(map(int, input().split()))
count = how_many_subsequences_that_sum_is(S, A)
if S == 0: count -= 1
print(count)
