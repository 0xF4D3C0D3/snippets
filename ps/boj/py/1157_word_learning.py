from collections import Counter

c = Counter(map(lambda x: x.upper(), input()))
k = sorted(c, key = lambda x: c[x])
if (len(k) == 1) or (c[k[-1]] != c[k[-2]]): print(k[-1].capitalize())
else: print('?')
