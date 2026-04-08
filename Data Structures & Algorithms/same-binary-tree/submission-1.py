# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:     
        res = True
        def dfs(p,q):
            if p and q:
                if p.val!=q.val:
                    return False
                resOne = dfs(p.left,q.left)
                resTwo = dfs(p.right,q.right)
                return resOne and resTwo
            elif p == None and q!=None:
                return False
            elif q==None and p!=None:
                return False
            else:
                return True


            
        res = dfs(p,q)
        return res 
        