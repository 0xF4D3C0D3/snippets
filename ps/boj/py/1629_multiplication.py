def fast_pow(A, B, MOD):
    """
    fast_pow = fast_pow(A, B//2) ** 2      (if B is even)
               fast_pow(A, B//2) ** 2 * A  (if B is odd )
               1                           (if B is zero)
    """
    if B == 0:
        return 1
    elif B%2 == 0:
        return (fast_pow(A, B//2, MOD) ** 2) % MOD
    else:
        return (fast_pow(A, B//2, MOD) ** 2 * A) % MOD
    
A, B, C = map(int, input().split())
print(fast_pow(A, B, C))
