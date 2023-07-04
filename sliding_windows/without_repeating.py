#  Longest Substring Without Repeating Characters


#   the idea is to use hasmap and store the values
#         check if the alphabet repeats or dont
#         if they do, just update the length
#         delete all those alphabet till that key


def longest_substring_without_repeating_characters(s):
    l, r = 0, 0
    l, r = 0, 0
    hashmap = {}
    max_length = 0

    while r < len(s):

        # check if the character is repeated using hashmap
        while r < len(s) and s[r] not in hashmap:
            hashmap[s[r]] = 1
            r += 1

        if r == len(s):
            max_length = max(max_length, len(hashmap))
            break
        else:
            max_length = max(max_length, len(hashmap))  # updating the length
            while l < len(s):  # looping till the repeating character is deleted
                if s[l] == s[r]:
                    del hashmap[s[l]]  # deleting the repeated character
                    l += 1
                    hashmap[s[r]] = 1
                    r += 1
                    break
                del hashmap[s[l]]
                l += 1
    return max_length  # returning the maximum length


# the length of 'abcde' or 'bcdea' is printed as 5
print(longest_substring_without_repeating_characters('aaabcdeab'))
