from collections import Counter

c = Counter(input())
c['9'] = c['6'] = (c['9']+c['6'])/2
print(int(c.most_common()[0][1]+0.5))
