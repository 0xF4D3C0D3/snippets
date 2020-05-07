start = f'{input():>02}'

get_next = lambda x: x[1] + str(sum(map(int, x))%10)
next_ = get_next(start)

count = 1
while next_ != start:
    count += 1
    next_ = get_next(next_)
print(count)
