N = int(input())

def solve(n):
    i = 666
    while True:
        if '666' in str(i):
            n -= 1
            if n == 0: return i
        i += 1
        
print(solve(N))
