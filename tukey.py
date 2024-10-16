import alg

def custom_median(nums):
    """Функция для нахождения медианы"""
    sorted_nums = alg.quicksort(nums)
    if len(nums) % 2 == 1:
        return sorted_nums[len(nums) // 2]
    else:
        return (sorted_nums[len(nums) // 2 - 1] + sorted_nums[len(nums) // 2]) / 2

def num_for_percentile(nums, p):
    """Функция для нахождения процентиля"""
    ans = (p / 100) * (len(nums) - 1)
    lowi = int(ans)
    upi = lowi + 1

    if ans != lowi and upi < len(nums):
        return (nums[lowi] + nums[upi]) / 2

    return nums[int(ans)]

def split_sample(nums, p):
    sorted_nums = alg.quicksort(nums)
    count = len(sorted_nums)
    median = custom_median(sorted_nums)

    if count % 2 == 1:
        left = sorted_nums[:count // 2]
        right = sorted_nums[count // 2 + 1:]
    else:
        left = sorted_nums[:count // 2]
        right = sorted_nums[count // 2:]

    if p == 50:
        return median
    if p < 50:
        return num_for_percentile(left, p * 2)
    else:
        return num_for_percentile(right, (p - 50) * 2)

"""def anomal_check(nums)
    up = split_sample(nums, 75)
    low = split_sample(nums, 25)
    for n in nums:
        if n > """
