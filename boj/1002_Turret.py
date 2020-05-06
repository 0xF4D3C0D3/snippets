import sys

# we don't need T. just read coordinates and radii line by line
tuples = [tuple(map(int, line.split())) for line in sys.stdin.readlines()[1:]]

for tup in tuples:
    x1, y1, r1, x2, y2, r2 = tup
    dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    
    # Cases are ordered by geometric probability
    # Case 1. two circles don't intersect (dist > r1+r2)
    #         or one circle is in another circle (dist < |r1-r2|)
    #         ∵ d + r1 < r2, d + r2 < r1 -> d < |r1-r2|
    if dist > r1+r2 or dist < abs(r1-r2):
        print(0)
    # Case 2. opposed to Case 1, two circles intersect
    elif r1+r2 > dist > abs(r1-r2):
        print(2)
    # Case 3. If their distance isn't zero, but their distance is identical to r1+r2 or |r1-r2|
    #         since if inner circle meets outer circle, dist+r1=r2, dist+r2=r1 -> dist=|r1-r2|
    elif dist != 0 and (dist == r1+r2 or dist == abs(r1-r2)):
        print(1)
    # Case 4. If their distance is zero and r1, r2 are identical,
    #         they are congruence, so number of answers would be infinity. In this case, -1
    else:
        print(-1)
