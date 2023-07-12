

def group_anagram(strs):
    # ## algorithm

    # - use loop
    # -sort elem and check if it exist in hashmap
    # -if true, append elem in hashmap[key]
    # -else hashmap[sorted(elem)]=[elem]

    hashmap = {}
    res = []
    for i in strs:
        sorted_elem = str(sorted(i))
        if sorted_elem in hashmap:
            hashmap[sorted_elem].append(i)
        else:
            hashmap[sorted_elem] = [i]

    for i in hashmap:
        res.append(hashmap[i])
    return res

    # time-complexity:O(n)+n*(100log(100))+k->O(n)
    # space-complexity:0(n)+0(n)


# prints [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
