from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def parse_input():
    get_next_int = lambda x: int(next(x))
    get_next_ints = lambda x: list(map(int, next(x).split()))

    lines = sys.stdin.readlines()

    gen_lines = (l for l in lines)
    T = get_next_int(gen_lines)
    for _ in range(T):
        _, K = get_next_ints(gen_lines)
        D = [0] + get_next_ints(gen_lines)
        G = defaultdict(set)
        for _ in range(K):
            from_, to = get_next_ints(gen_lines)
            G[to] |= {from_}
        W = get_next_int(gen_lines)
        yield G, D, W
        
def find_minimum_delay(G, D, to, tab):
    """
    find the minimum delay by using dp with tabulation
    G: Graph with which adjacent nodes are connected
    D: Delay for each nodes
    to: the last node we want
    """
    cost = 0
    
    # In here, we'll use top-down approach
    # this block traverses all node which has the destination as `to`
    for node in G[to]:
        cost = max(cost, (find_minimum_delay(G, D, node, tab) if tab[node] is None else tab[node]))
    
    # the cost of itself should be added too
    tab[to] = cost + D[to]
    return tab[to]

gen_case = parse_input()
for G, D, W in gen_case:
    tab = [None] * (len(D) + 1)
    print(find_minimum_delay(G, D, W, tab))
