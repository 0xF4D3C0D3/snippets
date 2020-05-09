def is_group(s):
    prev_chars = set()

    prev = ''
    for c in s:
        if c in prev_chars:
            if prev != c:
                return False
        else:
            prev_chars.add(c)
        prev = c
    return True

res = 0
for _ in range(int(input())):
    res += int(is_group(input()))
    
print(res)
