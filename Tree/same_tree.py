# -- algortihm

# travel through both trees at same time

self.sameTree = True


def dfs(p, q):
    if not p and q:
        self.sameTree = False
        return
    if p and not q:
        self.sameTree = False
        return
    if not p and not q:
        return
    else:
        if p.val != q.val:
            self.sameTree = False
        dfs(p.left, q.left)
        dfs(p.right, q.right)
        if self.sameTree == False:
            return


dfs(p, q)  # p and q are two diff trees
return self.sameTree
