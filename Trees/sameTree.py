"""
Idea:
Recursively compare both binary trees. If both nodes are null, return True. 
If only one is null or their values do not match, return False. 
Otherwise, recursively verify that both their left subtrees and right subtrees are identical.

Examples:
- Input: p = [1, 2, 3], q = [1, 2, 3] -> Output: True
- Input: p = [1, 2], q = [1, null, 2] -> Output: False

Complexity:
- Time: O(N) since each node in the trees is visited once.
- Space: O(H) for the recursion stack, where H is the height of the tree.
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not (p and q) or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
