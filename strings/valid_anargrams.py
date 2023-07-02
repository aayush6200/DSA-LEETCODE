
s='tea'
t='eat'
# An Anagram is a word or phrase formed by rearranging the\
#       letters of a different word or phrase, typically using all the original letters exactly once.


# using two hashmap and comparing both will provide answer


hashmap={}
hashmap2={}


for i in s:
    hashmap[i]=1+hashmap.get(i,0)
for i in t:
    hashmap2[i]=1+hashmap2.get(i,0)


print(True) if hashmap==hashmap2 else print 