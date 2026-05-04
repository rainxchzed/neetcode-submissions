/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun maxDepth(root: TreeNode?, count: Int = 0): Int {
        if (root == null){
            return count
        }

        val left = maxDepth(root.left, count + 1)
        val right = maxDepth(root.right, count + 1)

        if(left > right) {
            return left
        } else {
            return right
        }
    }
}
