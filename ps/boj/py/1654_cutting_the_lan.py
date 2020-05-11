# https://github.com/0xF4D3C0D3/snippets/blob/master/ps/boj/py/1654_cutting_the_lan.py

import sys

def binary_search_left(l, r, pred):
    while l < r:
        m = (l+r)//2
        if pred(m): l=m+1
        else: r=m
    return l

def get_how_many_lans_with_x_length(lans, x):
    return sum(l//x for l in lans)

def get_max_length(lans, N):
    def is_not_less_than_N_with_x_length(x):
        return get_how_many_lans_with_x_length(lans, x) >= N
    answer = binary_search_left(1, max(lans), is_not_less_than_N_with_x_length)
    while get_how_many_lans_with_x_length(lans, answer) < N:
        answer -= 1
    return answer

lines = sys.stdin.readlines()
_, N = map(int, lines[0].split())
lans = list(map(int, lines[1:]))
print(get_max_length(lans, N))
