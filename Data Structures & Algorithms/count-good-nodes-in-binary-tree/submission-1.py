# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root,prev):
            nonlocal res
            if root is None:
                return 0
            if root.val >= prev:
                res+=1
                print(root.val)
                prev = root.val
            dfs(root.left,prev)
            dfs(root.right,prev)
            return res
        dfs(root,root.val)
        return res







    





        