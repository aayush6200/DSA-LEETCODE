# algorithm

# use two pointers
# convert i in s to lowecase and check if two pointers i match


def valid_palindrome(s):
    l, r = 0, len(s)-1
    while r > l:
        if s[l].isalnum() == False:
            while l < r and s[l].isalnum() == False:
                l += 1
        if s[r].isalnum() == False:
            while r > l and s[r].isalnum() == False:
                r -= 1
        if l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))  # prints True
print(valid_palindrome("race a car"))  # prints False
