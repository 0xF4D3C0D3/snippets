x, y, w, h = map(int, input().split())
print(min(h-y, w-x, y, x))  # top, right, bottom, left respectively
