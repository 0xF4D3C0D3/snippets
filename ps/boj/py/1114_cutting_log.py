# https://github.com/0xF4D3C0D3/snippets/blob/master/algorithm/bisect.py
def binary_search_left(L, R, pred):
    while L < R:
        m = (L + R) // 2
        if pred(m):
            R = m
        else:
            L = m + 1
    return L


def get_predicate_to_cut(L, C, X):
    """
    currying a predicate for specific L, C, X to cut
    """

    def pred(max_length):
        """
        predicate checks whether this length is sufficient or not
        """
        count = 0
        diff = 0
        for i in range(1, len(X)):
            diff += X[i] - X[i - 1]
            if diff > max_length:  # if current chunk is longer than `max_length`
                count += 1  # cut it, and increase count by 1
                diff = X[i] - X[i - 1]  # now, the length of chunk is `X[i] - X[i-1]`

                # short-circuits
                if count > C:
                    return False
                if diff > max_length:
                    return False
        return count <= C

    return pred


def get_first_position(C, X, max_length):
    """
    returns first position to cut the log
    """
    count = 0
    last = L
    # from the end to the start
    for i in range(len(X) - 2, -1, -1):
        if last - X[i] > max_length:  # if current chunk is longer than `max_length`
            count += 1  # it should be cut
            last = X[i + 1]  # and also update the last cut position
    if count < C:
        last = X[1]  # if count is less than C, it's okay to cut from the start
    return last


def get_max_length_and_first_pos(L, C, X):
    """
    params:
        L (int): the length of a log
        C (int): the maximum count for cutting
        X (list[int]): the list of candidate positions to cut
    """
    sorted_X = [0, *sorted(X), L]
    max_length = binary_search_left(0, L, get_predicate_to_cut(L, C, sorted_X))
    first_pos = get_first_position(C, sorted_X, max_length)
    return max_length, first_pos


L, _, C = map(int, input().split())
X = map(int, input().split())

print(*get_max_length_and_first_pos(L, C, X))
