"""
Idea:
Recursively traverse the binary tree. For each node, swap its left and right children, 
then recursively call the function on both subtrees. If the node is None, return.

Examples:
- Input: root = [4, 2, 7, 1, 3, 6, 9] -> Output: [4, 7, 2, 9, 6, 3, 1]
- Input: root = [2, 1, 3] -> Output: [2, 3, 1]

Complexity:
- Time: O(N) since every node in the tree is visited once.
- Space: O(H) for the recursion stack, where H is the height of the tree (O(N) worst-case, O(log N) best-case).
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
