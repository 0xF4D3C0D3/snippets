a = [1, 2, 3, 5, 5, 9, 9, 9, 9, 9, 15]
#    0  1  2  3  4  5  6  7  8  9  10
pred_l = lambda i: a[i] < 9
pred_r = lambda i: a[i] > 9

def binary_search_left(L, R, pred):
    while L < R:
        m = (L+R)//2
        if pred(m): L = m+1
        else: R = m
    return L

def binary_search_right(L, R, pred):
    while L < R:
        m = (L+R)//2
        if pred(m): R = m
        else: L = m+1
    return R-1


print(binary_search_left(0, 10, pred_l), binary_search_right(0, 10, pred_r))
# (5, 9)
