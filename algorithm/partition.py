def partition(list_, k):
    """
    partition([1, 2, 3, 4], 2) -> [[1], [2, 3, 4]], [[1, 2], [3, 4]], ..., [[1, 3], [2, 4]], [[3], [1, 2, 4]]
    """
    if k == 1:  # base case 1: k == 1, just yield itself as a list
        yield [list_]
    elif k == len(list_):  # base case 2: k == len(list_), yield each item in the list wrapped in a list
        yield [[s] for s in list_]
    else:
        head, *tail = list_  # head = the first element, tail = the rest
        for p in partition(tail, k-1):  # case 1: head -> 1, partition(tail, k-1) -> k-1.
                                        # head + partition(tail, k-1) -> 1+k-1 -> k
            yield [[head], *p]
        for p in partition(tail, k):  # case 2: head -> 1, partition(tail, k) -> k.
                                      # bloat x to [e1, e2, e3] -> [[x+e1, e2, e3], [e1, x+e2, e3], [e1, e2, x+e3]]
            for i in range(len(p)):
                yield p[:i] + [[head] + p[i]] + p[i+1:]  # bloat head to partition(tail, k) -> k
