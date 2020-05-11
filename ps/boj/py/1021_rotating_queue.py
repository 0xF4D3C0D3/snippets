ans = 0
N, _ = map(int, input().split())

# T is where to get
# you can think of this as rotatable queue
# and the input is one-based index so adjust it
T = [e-1 for e in map(int, input().split())]

while T:
    # head is the first position to pop in the remain elements
    head = T[0]
    if head == 0:  # if head is zero, then the number that was at the position is at the first now
        T = [e-1 for e in T[1:]]  # then pop the head and adjust other positions
        N -= 1  # and also adjust total number of positions
    else:  # if head isn't zero, then the number that was at the position isn't at the first yet
        # if head <= N//2 then the position could get to the first faster by rotating left, otherwise right
        offset = -head if head <= N//2 else N-head
        ans += abs(offset)
        
        # with modulo operation, we can mimic a rotating queue faster
        T = [(e+offset)%N for e in T]
print(ans)
