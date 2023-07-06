# logic is to check for substring for every character
# for even length, l,r=i,i+1 initially

# for odd length, l,r=i,i initially
def longest_palindromic_substring(s):
    longest_substring = ''
    for i in range(len(s)):
        # for even length in palindromic substring
        l, r = i, i+1

        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break

        if len(s[l+1:r]) > len(longest_substring):
            longest_substring = s[l+1:r]

        # for odd length in palindromic substring

        l, r = i, i

        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break

        if len(s[l+1:r]) > len(longest_substring):
            longest_substring = s[l+1:r]
    return longest_substring


# prints bab . bab is also valid solution
print(longest_palindromic_substring('babaaa'))
