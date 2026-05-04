/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun inorderTraversal(root: TreeNode?, res: MutableList<Int> = mutableListOf()): List<Int> {
        if(root == null) {
            return listOf<Int>()
        }

        inorderTraversal(root.left, res)
        res.add(root.`val`)
        inorderTraversal(root.right, res)

        return res.toList()
    }
}
