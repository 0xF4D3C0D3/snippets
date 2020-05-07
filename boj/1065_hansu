def is_hansu(n):
    """
    if each digits of a positive number satisfies arithmetic progression, the number is hansu
    an arithmetic progression is a sequence that has a constant consecutive difference
    """
    if n < 10:
        return True
    nums = list(map(int, str(n)))
    diff = nums[1] - nums[0]
    start = nums[0]
    for idx, num in enumerate(nums):
        if start + diff*idx != num:
            return False
    return True

# the n is less than 1000, so we can use bruteforce as the worst case is but 4*1000
print(sum([is_hansu(i) for i in range(1, int(input())+1)]))
