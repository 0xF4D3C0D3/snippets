def convert_to_int(mat):
    return int(''.join(''.join(map(str, r)) for r in mat), 2)


def translate(mat, L, r, c):
    A = 2**(L**2)
    
    if c > 0:
        mat = rotate(mat, L, 1)
        mat = (mat>>(L*c))%A
        mat = rotate(mat, L, 3)
    else:
        mat = rotate(mat, L, 3)
        mat = (mat<<(L*-c))%A
        mat = rotate(mat, L, 1)
        
    if r > 0: mat = (mat<<(L*r))%A
    else:     mat = (mat>>(L*-r))%A
    return mat


def rotate(mat, L, n):
    for _ in range(n):
        m = list(f'{mat:0{L*L}b}')
        for c in range(0, L//2):
            for r in range(c, L-c-1):
                i = (c)    *L + r
                j = (r)    *L + L-1-c
                k = (L-1-c)*L + L-1-r
                l = (L-1-r)*L + c
                m[i], m[j], m[k], m[l] = m[l], m[i], m[j], m[k]
        m = int(''.join(m), 2)
    return m


def check_all_cases(key, lock, L):
    A = 2**(L**2)
    
    for i in range(4):
        key = rotate(key, L, 1)
        for r in range(-L, L):
            for c in range(-L, L):
                if translate(key, L, r, c) ^ lock == A-1:
                    return True
    return False


def expand(mat, D, L):
    return [[0]*D]*(D-L) + [[0]*(D-L) + r for r in mat]


def solution(key, lock):
    N = len(lock[0])
    M = len(key[0])
    int_key  = convert_to_int(expand(key, N, M))
    int_lock = convert_to_int(lock)
    return check_all_cases(int_key, int_lock, N)
