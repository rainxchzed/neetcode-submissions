# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], count: int = 0) -> int:
        if root == None:
            return count
            
            
        right = self.maxDepth(root.right, count + 1)
        left = self.maxDepth(root.left, count + 1)

        if right > left:
            return right
        else:
            return left

