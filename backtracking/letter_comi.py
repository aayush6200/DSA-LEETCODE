
# use hashmap to store letters that maps to number
# use backtracking to generate all outputs


hashmap = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
res = []
digits = '23'


def backtrack(start, cur):
    if len(digits) == 0:
        return []
    if len(cur) == len(digits):
        res.append(cur)
    else:
        for i in range(start, len(digits)):
            for j in hashmap[digits[i]]:
                backtrack(i+1, cur+j)


backtrack(0, '')
print(res)  # prints ["ad","ae","af","bd","be","bf","cd","ce","cf"]
