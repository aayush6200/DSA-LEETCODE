# algorithm:
# on every s[i], check if s[i] is in hashmap
hashmap = {')': '(', '}': '{', ']': '['}
stack = []


def valid_parenthesis(s):

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            # checking if parenthesis balances
            if i in hashmap and hashmap[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    return True if len(stack) == 0 else False


print(valid_parenthesis("()[]{}"))  # prints True

print(valid_parenthesis("(]"))  # prints False
