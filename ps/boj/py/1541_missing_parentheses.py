import re
E = input()
E2 = re.sub('(^|\+|-)0+(\d)', '\g<1>\g<2>', E)  # because the number could start 0
E3 = re.sub('((?:\d+\+?)+)', '(\g<1>)', E2)     # make the minus term as big as possible
answer = eval(E3)
print(answer)
