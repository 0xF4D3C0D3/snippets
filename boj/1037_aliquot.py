_=input()
p=sorted(map(int,input().split()))

# If p is the sorted list of proper divisors,
# the original number of p is p[0] * p[-1], p[1] *[-2], ...
print(p[0]*p[-1])
