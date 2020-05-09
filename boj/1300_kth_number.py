"""
# Overview
There is a NxN matrix and the value at ith row and jth column is i * j
then put its all elements into the 1D list B and sort it

When given k, What's B[k]?

# Approach
N can be up to 10^5 so if we try to make a NxN matrix we would get MLE
Instead, let's assume there is a such matrix N
and if we can know how many numbers less than x then the number is B[k] if the number is k

As you know, the thing is getting how many numbers less than x
So we need to do as little as possible, that's why we'll use parametric search here

the search space would be 1 ~ min(10**9, N*N) from the start
and if we bisect it we can find the solution in O(Nlog(N^2))  ∵ getting the number is O(n)

# Solution
1. define a function that returns how many numbers less than x
1-1. from 1 to N, at every ith iteration, accumulate lesser value between N and x//i
1-2. because, at ith row, the number of elements less than x would be N or x//i
2. define another function that the number of elements less than x is less than k
3. bisect the search space with the predicate in 2
"""

def how_many_numbers_less_than(N, x):
    return sum(min(N, x//i) for i in range(1, min(x+2, N+1)))

def is_less_than_k(x):
    return how_many_numbers_less_than(N, x) < k

def binary_search_left(L, R, pred):
    while L < R:
        m = (L+R)//2
        if pred(m): L = m+1
        else: R = m
    return L

def get_kth_number(N, k):
    return binary_search_left(1, min(10**9, N*N), is_less_than_k)

N = int(input())
k = int(input())
print(get_kth_number(N, k))
