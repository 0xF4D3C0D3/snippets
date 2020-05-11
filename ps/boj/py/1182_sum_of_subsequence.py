# https://github.com/0xF4D3C0D3/snippets/blob/master/boj/1182_sum_of_subsequence.py

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

N, S = map(int, input().split())
L = list(map(int, input().split()))

count = sum(sum(sub) == S for sub in powerset(L))
print(count)
