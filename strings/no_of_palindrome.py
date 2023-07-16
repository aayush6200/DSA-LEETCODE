# algorithm:
# inside a for loop
# calculate palindrom for each s[i]

def no_of_palindrome(s):
    count = 0

    for i in range(len(s)):
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count


print(no_of_palindrome('abc'))  # prints 3


# time-complexity=O(n^2)
# space-complexity=O(1)
