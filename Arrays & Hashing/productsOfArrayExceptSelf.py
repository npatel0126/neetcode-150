"""
Idea:
Compute the product of all elements except self without using division by using a two-pass approach. 
In the first pass (prefix pass), store the cumulative product of all elements to the left of each index. 
In the second pass (postfix pass), multiply by the cumulative product of all elements to the right of each index.

Examples:
- Input: nums = [1, 2, 3, 4] -> Output: [24, 12, 8, 6]
- Input: nums = [-1, 1, 0, -3, 3] -> Output: [0, 0, 9, 0, 0]

Complexity:
- Time: O(N) where N is the length of the array, since we iterate through the array twice.
- Space: O(1) auxiliary space (excluding the result array).
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
