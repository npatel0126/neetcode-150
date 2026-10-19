"""
Idea:
Find the indices of the two numbers in a sorted array that add up to a target value using a two-pointer approach. 
Initialize one pointer at the beginning (`left`) and the other at the end (`right`). If the sum of the values at both 
pointers is greater than the target, decrement the right pointer. If the sum is less than the target, increment 
the left pointer. Otherwise, return the 1-based indices.

Examples:
- Input: numbers = [2, 7, 11, 15], target = 9 -> Output: [1, 2]
- Input: numbers = [2, 3, 4], target = 6 -> Output: [1, 3]

Complexity:
- Time: O(N) where N is the length of the numbers array, as the pointers move inward at most N steps.
- Space: O(1) auxiliary space.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l +=1 
            else:
                return [l + 1, r + 1]
