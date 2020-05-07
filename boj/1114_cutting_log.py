# https://www.topcoder.com/community/competitive-programming/tutorials/binary-search
# to get least x for which pred(x) is true
def binary_search(lo, hi, pred):
    while lo < hi:
        mid = (lo+hi) // 2
        if pred(mid): hi = mid
        else:
            r = lo
            lo = mid+1
    return r

# get a predicate for verifying the max length
def get_predicate(L, C, xs):
    
    # closure to be returned
    def cut_log(max_length, xs=xs):
        diff  = 0
        count = 0
        for i in range(0, len(xs)-1):
            diff += xs[i+1] - xs[i]

            # if this is the time to cut
            if diff > max_length:
                # cut it
                count += 1
                diff = xs[i+1] - xs[i]
                
                if diff > max_length: return False    
                if count > C: return False
        return count <= C
    
    return cut_log

# get the first matching position
def get_first_match(max_length, xs):
    count = 0
    last = L

    # from the last position, verify the max_length
    for i in range(len(xs)-2, -1, -1):
        # if current position can't be cut
        # increase the count and set the last to the previous position
        if last - xs[i] > max_length:
            count += 1
            last = xs[i+1]

    # up to first position, if the count is less than C
    # then it's safe to start from the first position
    if (count < C): last = xs[1]
        
    return last

# the solver function
def solve(L, C, xs):
    # for convenience' sake, add the both-end position
    xs = [0] + sorted(xs) + [L]

    # get the max length of the shortest part
    max_length = binary_search(0, L, get_predicate(L, C, xs))

    # get the first position meets the above condition
    first = get_first_match(max_length, xs)

    print(max_length, first)

# L -> the length of the log
# C -> the max number of times to cut
# xs -> the sorted list of possible positions to cut
L, _, C = map(int, input().split())
xs = map(int, input().split())

solve(L, C, xs)
