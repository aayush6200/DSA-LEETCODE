# algorithm
# try to create a sorted array
# if after travelling through whole tree, sorted array , true
# else false
res = []


def dfs(root):
    if not root:
        return
    else:
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)


dfs(root)

for i in range(len(res)):
    if i+1 < len(res) and res[i+1] <= res[i]:
        return False
return True
