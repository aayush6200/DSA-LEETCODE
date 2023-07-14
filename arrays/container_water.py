
# algortithm

# -use two pointers as l,r
# -calculate area for min(height[l],height[r])*(r-l+1)

def most_water(height):
    maxArea = 0

    l, r = 0, len(height)-1

    while l < r:
        # calculate area
        length = height[l] if height[r] > height[l] else height[r]
        breadth = r-l
        maxArea = max(maxArea, length*breadth)
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    return maxArea


print(most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # prints height 49
