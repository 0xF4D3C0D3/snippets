# https://github.com/0xF4D3C0D3/snippets/blob/master/boj/1208_sum_of_subsequence_2.py

from collections import Counter
import itertools


def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def how_many_subsequences_that_sum_is(S, A):
    # Split A into two parts so that we can perform it in O(2^(N/2)) instead of O(2^N)
    m = len(A)//2
    L, R = A[:m], A[m:]
    
    # pre calculate the sum and its count of all subsets from L
    c = Counter(sum(s) for s in powerset(L))
    
    # we want to know the number of subsequences whose sum is S
    # so let's call sums of subsequences from L and R l, r respectively
    # then answer is sum of all c[x] such that x+r=S, in other words, sum(c[S-r] for r in powerset(R)
    return sum(c[S-sum(s)] for s in powerset(R))

_, S = map(int, input().split())
A = list(map(int, input().split()))

count = how_many_subsequences_that_sum_is(S, A)
if S == 0: count -= 1
print(count)
