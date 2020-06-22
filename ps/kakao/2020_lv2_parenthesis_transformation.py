from collections import deque

def split(w):
    dq = deque(w[0])
    i = 1
    for c in w[1:]:
        if dq[-1] == c: dq.append(c)
        else: dq.pop()
        i += 1
        if not dq: break
    return w[:i], w[i:]

def solution(w):
    if not w: return w
    u, v = split(w)
    
    if u[0] == '(': u += solution(v) 
    else:           u  = '(' + solution(v) + ')' + u[1:-1].replace('(', '_').replace(')', '(').replace('_', ')')
        
    return u
