def solve(d):
    sqrt_d = round(d**0.5)
    if sqrt_d**2 - sqrt_d + 1 <= d <= sqrt_d**2:
        return sqrt_d*2-1
    return sqrt_d*2

T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    print(solve(end - start))
