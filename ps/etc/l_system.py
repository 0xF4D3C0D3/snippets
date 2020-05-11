def l_system_gen(x, rule):
    table = str.maketrans(rule)
    while True:
        yield x
        x = x.translate(table)

l_system = l_system_gen('AB', {'A':'AB', 'B': 'A'})

print(next(l_system))  # AB
print(next(l_system))  # ABA
print(next(l_system))  # ABAAB
print(next(l_system))  # ABAABABA
