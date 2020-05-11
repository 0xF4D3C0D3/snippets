import sys

white_first = ['WBWBWBWB',
               'BWBWBWBW',]*4

black_first = ['BWBWBWBW',
               'WBWBWBWB',]*4

lines = sys.stdin.readlines()
H, W = map(int, lines[0].split())
lines = lines[1:]

answer = 9e9
for r in range(H-7):
    for c in range(W-7):
        for which_first in [black_first, white_first]:
            get_how_many_tiles_to_paint = sum([sum(row) for row in [[c1 != c2 for c1, c2 in zip(r1[c:c+8], r2)] for r1, r2 in zip(lines[r:r+8], which_first)]])
            answer = min(answer, get_how_many_tiles_to_paint)
print(answer)
