"""
Idea:
Use binary search with left and right pointers to repeatedly divide the search space in half. 
Compare the middle element to the target: if it matches, return its index; 
if the target is larger, search the right half; otherwise, search the left half.

Examples:
- Input: nums = [-1, 0, 3, 5, 9, 12], target = 9 -> Output: 4
- Input: nums = [-1, 0, 3, 5, 9, 12], target = 2 -> Output: -1

Complexity:
- Time: O(log N) because the search space is halved in each iteration.
- Space: O(1) using constant extra space for pointers.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return -1
