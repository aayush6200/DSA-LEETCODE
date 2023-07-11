# algorithm is to use hashmap
# check for duplicate


def contains_duplicate(nums):
    hashmap = {}
    for i in nums:
        if i in hashmap:
            return True
        hashmap[i] = i
    return False

    # time complexity:O(n)
    # space complexity:O(n)

    # ## another algorithm is to sort elem and check if element exist

    # nums.sort()

    # for i in range(len(nums)):
    #     if i+1<len(nums):
    #         if nums[i]==nums[i+1]:
    #             return True
    # return False


print(contains_duplicate([1, 2, 5, 2, 3]))  # prints True

print(contains_duplicate([1, 2, 3, 7, 4, 5]))  # prints False
