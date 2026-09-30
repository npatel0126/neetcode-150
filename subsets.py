"""
Idea:
Use backtracking (DFS) to generate all possible subsets by making a binary choice at each index: 
either include the current number in the subset or exclude it. 
Recursively explore both branches and append a copy of the subset to the result when the end of the array is reached.

Examples:
- Input: nums = [1, 2, 3] -> Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
- Input: nums = [0] -> Output: [[], [0]]

Complexity:
- Time: O(N * 2^N) since there are 2^N possible subsets and it takes O(N) time to copy each subset to the result.
- Space: O(N) for the recursion stack and the temporary subset storage.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subs = []
        curr_subs = []

        def backtrack(i): 
            if i >= len(nums):
                all_subs.append(curr_subs.copy())
                return
            
            # Include the current element
            curr_subs.append(nums[i])
            backtrack(i + 1)

            # Exclude the current element (backtrack)
            curr_subs.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return all_subsets
