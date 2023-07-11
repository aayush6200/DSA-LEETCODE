

def three_sum(nums):
    # algorithm
    # sort the nums:
    nums.sort()
    # create set to check if duplicate elem is present
    res = set()
    # use three pointers to check for the results
    i = 0
    while i < len(nums):
        j = i+1
        k = len(nums)-1
        while j < k:
            if nums[j]+nums[k]+nums[i] < 0:
                j += 1
            elif nums[j]+nums[k]+nums[i] > 0:
                k -= 1
            else:
                res.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1

        i += 1
    return res


# prints([(-1, 0, 1), (-1, -1, 2)])
print(list(three_sum(([-1, -1, 2, 0, 1]))))
