# Algorithm

# - if the total sum is <0 and nums[i]>=0, just start from that point
# -if sum+nums[i]<sum and sum<0, use step 1
# update maxSum


def max_subarray(nums):
    maxSum = -1000000000
    Sum = 0
    i = 0

    while i < len(nums):
        if (Sum+nums[i] < Sum and Sum < 0) or (Sum < 0 and nums[i] >= 0):
            Sum = nums[i]
        else:
            Sum += nums[i]
        maxSum = max(Sum, maxSum)
        i += 1
    return maxSum


# prints 6 bcz The subarray [4,-1,2,1] has the largest sum 6.
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
