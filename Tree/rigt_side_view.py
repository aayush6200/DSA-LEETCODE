# if not root:
#     print([])

# # algorithm
# # travel from right of tree
# # keep track of height
# # if height>prev_maxHeight,append the new node in res

# res=[root.val]
# self.height=1

# def dfs(root,height):
#     if not root:
#         return
#     else:
#         if height>self.height:
#             res.append(root.val)
#             self.height+=1
#         dfs(root.right,height+1)
#         dfs(root.left,height+1)
# dfs(root,1)
# return res
