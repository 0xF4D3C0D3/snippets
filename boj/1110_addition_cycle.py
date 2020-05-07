start = f'{input():>02}'

get_next = lambda x: x + str(sum(map(int, start))%10)
next_ = get_next(start[1])

count = 1
while next_ != start:
    count += 1
    next_ = get_next(next_[1])
print(count)
