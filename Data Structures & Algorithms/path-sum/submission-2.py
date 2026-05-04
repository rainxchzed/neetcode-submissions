# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.rec(root, targetSum, 0)
    
    def rec(self, root: Optional[TreeNode], targetSum: int, curr: int) -> bool:
        if not root:
            return False
        curr += root.val
        print(root.val, curr)
    
        if not root.left and not root.right:
            return curr == targetSum
        if self.rec(root.left, targetSum, curr):
            return True
        if self.rec(root.right, targetSum, curr):
            return True
        
        return False
