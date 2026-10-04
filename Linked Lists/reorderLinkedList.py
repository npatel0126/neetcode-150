"""
Idea:
Split the linked list into two halves using the slow and fast pointer technique. 
Reverse the second half of the list in-place, then alternately merge the nodes 
from the first and second halves together.

Examples:
- Input: head = [1, 2, 3, 4] -> Output: [1, 4, 2, 3]
- Input: head = [1, 2, 3, 4, 5] -> Output: [1, 5, 2, 4, 3]

Complexity:
- Time: O(N) where N is the number of nodes in the linked list.
- Space: O(1) as the list is reordered in-place using constant extra space.
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp 

        # Merge the two halves
        first, second = head, prev
        while second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
