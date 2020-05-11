def fibo(n):
    """
    return a pair, former is number of zeros would be called and
    latter is number of ones called
    """
    
    # we'll use 1D tabulation dp with some base cases
    tab = [(1, 0), (0, 1)] + [None] * (n-1)
    
    # use base case by dp
    if n <= 1:
        return tab[n]

    # this logic is just advanced version of basic fibonacci
    for i in range(2, n+1):
        tab[i] = (tab[i-2][0]+tab[i-1][0], tab[i-2][1]+tab[i-1][1])

    return tab[n]

T = int(input())
for _ in range(T):
    print(*fibo(int(input())))
