# https://github.com/0xF4D3C0D3/snippets/edit/master/boj/1316_group_word_checker.py

def is_group(s):
    prev_chars = set()
    for c, lead in zip(s, s[1:]+'_'):
        if c != lead:
            if c in prev_chars: return False
            prev_chars.add(c)
    return True

print(sum(is_group(input()) for _ in range(int(input()))))
