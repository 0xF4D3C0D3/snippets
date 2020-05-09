"""
# Overview

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…  	…
3/1	3/2	3/3	…  	…  	…
4/1	4/2	…       …  	…  	…
5/1	…	…  	…	…  	…
…	… 	…	…  	…  	…
Above is infinite sized matrix enumerating fractions in zigzag order like below
1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> …
and let's number them 1, 2, 3, …

So how can we find the x-th fraction when x is given?

# Approach
Let's rotate it 45 degree and it would looks like below
        1/1         ... 1
      1/2 2/1       ... 2
    3/1 2/2 1/3     ... 3
  1/4 2/3 3/2 1/4   ... 4
5/1 4/2 3/3 2/4 1/5 ... 5
As you can see the odd floors start from n/1, whereas even floors start from 1/n
and there are n fractions in the n-th floor so we can make a general term like below
the index of start at n-th floor = 1 + n(n+1)//2  ∵ it's difference sequence and its common difference is 1 and first term is 1

# Solution
1. Find the maximum n such that n(n+1) <= 2(x-1)
2. Find the offset with |x - (1 + n(n+1)//2)|
3. Let's a = n-offset, b = 1+offset
4. Print b/a if n is even number else a/b
"""

