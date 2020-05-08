import sys

def get_minimum_cost_to_paint(n, arr):
    ans = arr[0]
    for i in range(1, n):
        ans = [arr[i][0] + min(ans[1], ans[2]),  # at ith house, you can keep track of cost of each color up to i
               arr[i][1] + min(ans[0], ans[2]),  # however, we don't need to know about all previous costs
               arr[i][2] + min(ans[0], ans[1])]  # instead, we'll use just only previous cost
    return min(ans)

N = int(input())
arr = [list(map(int, line.split())) for line in sys.stdin.readlines()]
print(get_minimum_cost_to_paint(N, arr))
