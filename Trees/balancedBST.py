"""
Idea:
Use bottom-up DFS to compute the height of each node while simultaneously checking if subtrees are balanced. 
If any subtree has a height difference greater than 1, return -1 to short-circuit and propagate 
the failure up the recursion tree. If the traversal completes without returning -1, the tree is balanced.

Examples:
- Input: root = [3, 9, 20, null, null, 15, 7] -> Output: True
- Input: root = [1, 2, 2, 3, 3, null, null, 4, 4] -> Output: False

Complexity:
- Time: O(N) since every node in the binary tree is visited once.
- Space: O(H) for the recursion stack, where H is the height of the tree.
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            
            bal_factor = left_height - right_height
            
            if abs(bal_factor) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
            
        return dfs(root) != -1
