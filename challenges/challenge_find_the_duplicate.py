def find_duplicate(nums):
    if not (isinstance(nums, list)):
        return False
    nums.sort()
    repeats = 0
    for i in range(len(nums)-1):
        if isinstance(nums[i], str) or nums[i] < 0:
            return False
        if nums[i] == nums[i+1]:
            repeats += 1
            return nums[i]
    return repeats_verify(repeats)


def repeats_verify(repeats):
    if repeats == 0:
        return False
