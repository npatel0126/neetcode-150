"""
Idea:
Recursively find the maximum depth of the left and right subtrees. The depth of the current 
tree is 1 plus the maximum of the left and right subtree depths. An empty tree has a depth of 0.

Examples:
- Input: root = [3, 9, 20, null, null, 15, 7] -> Output: 3
- Input: root = [1, null, 2] -> Output: 2

Complexity:
- Time: O(N) since every node in the binary tree is visited once.
- Space: O(H) for the recursion stack, where H is the height of the tree.
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
