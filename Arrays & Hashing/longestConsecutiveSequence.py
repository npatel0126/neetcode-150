"""
Idea:
Find the length of the longest consecutive elements sequence by converting the array into a hash set for O(1) lookups. 
For each number, check if it is the start of a sequence (i.e., `num - 1` is not in the set). If it is the start, 
count consecutive numbers upward using a while loop and update the maximum length found.

Examples:
- Input: nums = [100, 4, 200, 1, 3, 2] -> Output: 4 (Sequence: [1, 2, 3, 4])
- Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] -> Output: 9

Complexity:
- Time: O(N) where N is the number of elements in the array, as each number is processed a constant number of times.
- Space: O(N) to store the elements in the hash set.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            # check if it is the start of a sequence
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                max_length = max(length, max_length)
                
        return max_length
