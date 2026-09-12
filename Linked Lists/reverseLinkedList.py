"""
Idea:
Use two pointers, curr and prev, to iterate through the linked list. 
For each node, temporarily store the next node, reverse the current node's pointer to prev, 
then advance prev and curr. Return prev as the new head when curr reaches the end.

Examples:
- Input: head = [1, 2, 3, 4, 5] -> Output: [5, 4, 3, 2, 1]
- Input: head = [1, 2] -> Output: [2, 1]

Complexity:
- Time: O(N) because we traverse the linked list of length N once.
- Space: O(1) using constant extra space for pointers.
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
