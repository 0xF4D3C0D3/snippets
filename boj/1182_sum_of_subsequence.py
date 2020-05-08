from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

N, S = map(int, input().split())
L = list(map(int, input().split()))

count = 0
for sub in list(powerset(L))[1:]:
    if sum(sub) == S:
        count +=1

print(count)
