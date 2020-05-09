# https://github.com/0xF4D3C0D3/snippets/blob/master/boj/1193_finding_fraction.py

"""
# Overview

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…  	…
3/1	3/2	3/3	…  	…  	…
4/1	4/2 …  	…  	…   …
5/1	…	…  	…	…  	…
…	… 	…	…  	…  	…
Above is infinite sized matrix enumerating fractions in zigzag order like below
1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> …
and let's number them 1, 2, 3, …

So how can we find the x-th fraction when x is given?

# Approach
Let's rotate it 45 degree and it would looks like below
        1/1         ... 0
      1/2 2/1       ... 1
    3/1 2/2 1/3     ... 2
  1/4 2/3 3/2 1/4   ... 3
5/1 4/2 3/3 2/4 1/5 ... 4
As you can see the odd floors start from 1/n, whereas even floors start from n/1
and there are n fractions in the n-th floor so we can make a general term like below
the index of start at n-th floor = 1 + n(n+1)//2  ∵ it's difference sequence and its common difference is 1 and first term is 1

# Solution
1. Find the maximum n such that n(n+1) <= 2(x-1)
2. Find the offset with 1 + |x - (1 + n(n+1)//2)|
3. Let's a = 1+n-offset, b = 1+offset
4. Print a/b if n is even number else b/a
"""

def find_n(x):
    n = int((2*(x-1))**0.5)
    while n*(n+1) > 2*(x-1):
        n -= 1
    return n

x = int(input())
n = find_n(x)                                # 1
offset = abs(x - (1 + n*(n+1)//2))           # 2
a, b = 1+n-offset, 1+offset                  # 3
print(f'{a}/{b}' if n%2==0 else f'{b}/{a}')  # 4 
