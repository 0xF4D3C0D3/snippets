import sys
print(''.join(sorted(set(sys.stdin.readlines()[1:]), key=lambda x: (len(x), x))))
