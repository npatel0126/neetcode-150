"""
Idea:
Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare) with two pointers: slow and fast. 
The slow pointer advances by one step and the fast pointer by two steps. If there is a cycle, 
the fast pointer will eventually wrap around and meet the slow pointer. If there is no cycle, 
fast will reach the end of the list.

Examples:
- Input: head = [3, 2, 0, -4], pos = 1 -> Output: True (tail connects to node index 1)
- Input: head = [1], pos = -1 -> Output: False (no cycle)

Complexity:
- Time: O(N) since the pointers traverse at most N nodes before meeting or reaching the end.
- Space: O(1) using only constant extra space for the two pointer variables.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
