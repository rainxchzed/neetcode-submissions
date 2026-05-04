/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        if(root == null) return listOf<List<Int>>()

        val queue: Queue<TreeNode> = ArrayDeque()
        val res = mutableListOf<List<Int>>()

        queue.add(root)
        res.add(listOf(root!!.`val`))

        var level = 0

        while (queue.size > 0) {
            var currNodes = mutableListOf<Int>()
            for (i in 0..queue.size-1) {
                val r = mutableListOf<Int>()
                val curr = queue.poll()
                if(level > 0) {
                    
                    currNodes.add(curr!!.`val`)
                }

                if (curr?.left != null) {
                    queue.add(curr.left)
                }

                if (curr?.right != null) {
                    queue.add(curr.right)
                }
            }

            if(currNodes.size > 0) {
                res.add(currNodes)
            }

            level++
        }

        return res.toList()
    }
}
