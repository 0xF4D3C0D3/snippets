def solve(string, l):
    if not string: return ''
    token = string[:l]
    cnt = 0
    for i in range(0, len(string), l):
        if string[i:i+l] == token: cnt += 1
        else: break
    return f'{cnt if cnt>1 else ""}{token}' + solve(string[l*cnt:], l)

def solution(s):
    if len(s) == 1: return 1
    return min(len(solve(s, l)) for l in range(1, len(s)//2+1))
