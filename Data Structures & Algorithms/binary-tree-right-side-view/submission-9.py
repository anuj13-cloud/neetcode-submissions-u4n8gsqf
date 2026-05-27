# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels=defaultdict(list)

        def dfs(root,level):
            nonlocal levels

            if not root:
                return 
            levels[level].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,0)
        arr = list(levels.values())
        res=[]
        for i in arr:
            res.append(i[-1])
        return res
