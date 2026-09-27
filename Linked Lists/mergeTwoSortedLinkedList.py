"""
Idea:
Use a dummy node to build the merged linked list. Iterate through both lists using two pointers, 
appending the smaller node's value to the tail and advancing that pointer. Once one list is exhausted, 
attach the remaining portion of the other list directly to the tail.

Examples:
- Input: list1 = [1, 2, 4], list2 = [1, 3, 4] -> Output: [1, 1, 2, 3, 4, 4]
- Input: list1 = [], list2 = [] -> Output: []
- Input: list1 = [], list2 = [1, 2] -> Output: [1, 2]

Complexity:
- Time: O(N + M) where N and M are the lengths of the two linked lists, as every node is visited once.
- Space: O(1) by reusing existing nodes and only maintaining pointers.
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return head.next
