a = [1, 2, 3, 5, 5, 9, 9, 9, 9, 9, 15]
#    0  1  2  3  4  5  6  7  8  9  10
pred_l = lambda i: a[i] < 9
pred_r = lambda i: a[i] > 9

def binary_search_left(l, r, pred):
    while l < r:
        m = (l+r)//2
        if pred(m): l=m+1
        else: r=m
    return l

def binary_search_right(l, r, pred):
    while l < r:
        m = (l+r)//2
        if pred(m): r=m
        else: l=m+1
    return r-1


print(binary_search_left(0, 10, pred_l), binary_search_right(0, 10, pred_r))
# (5, 9)
