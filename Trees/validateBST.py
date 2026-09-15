"""
Idea:
Use a recursive helper function with boundary limits (left_val and right_val) to ensure 
every node's value falls within its valid range. When traversing left, update the upper bound 
to the current node's value. When traversing right, update the lower bound to the current node's value.

Examples:
- Input: root = [2, 1, 3] -> Output: True
- Input: root = [5, 1, 4, null, null, 3, 6] -> Output: False

Complexity:
- Time: O(N) since every node in the tree is visited once.
- Space: O(H) for the recursion stack, where H is the height of the tree.
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left=float('-inf'), right=float('inf')):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        
        return validate(root)
