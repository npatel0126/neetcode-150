"""
Idea:
Use a Hash Set to track visited numbers while iterating through the array. 
If a number is already in the set, a duplicate exists (return True). 
Otherwise, add it to the set. If the loop completes, all elements are unique (return False).

Examples:
- Input: nums = [1, 2, 3, 1] -> Output: True
- Input: nums = [1, 2, 3, 4] -> Output: False

Complexity:
- Time: O(N) since we traverse the list once with O(1) set operations.
- Space: O(N) to store the set in the worst case.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for num in nums:
            if num in dup:
                return True
            else:
                dup.add(num)

        return False
