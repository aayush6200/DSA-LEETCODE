
# algo-
# travel left and right
# swap nodes

def dfs(root):
    if not root:
        return
    else:
        dfs(root.left)
        dfs(root.right)
        root.left, root.right = root.right, root.left


dfs(root)
return root


# time-complexity =O(n)
# space-complexity =O(1)
