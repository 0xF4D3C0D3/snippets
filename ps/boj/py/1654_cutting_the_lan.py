import sys

def binary_search_right(l, r, pred):
    while l < r:
        m = (l+r)//2
        if pred(m): r=m
        else: l=m+1
    return r-1

def get_how_many_lans_with_x_length(lans, x):
    return sum(l//x for l in lans)

def get_max_length(lans, N):
    def is_less_than_N_with_x_length(x):
        return get_how_many_lans_with_x_length(lans, x) < N
    answer = binary_search_right(1, max(lans), is_less_than_N_with_x_length)
    return answer

lines = sys.stdin.readlines()
_, N = map(int, lines[0].split())
lans = list(map(int, lines[1:]))
print(get_max_length(lans, N))
