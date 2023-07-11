# -> algorithm-1:

# use hashmap
# target=key+i
# so keep checking i in nums.
# if target-i==key, return hashmap[key]


def two_sum(target, nums):
    hashmap = {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i


print(two_sum(5, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # prints [0,1]

# time-complexity:O(n)
# space-complexity:o(n)
