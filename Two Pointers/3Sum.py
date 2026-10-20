"""
Idea:
Find all unique triplets in the array that sum to zero by first sorting the array. 
Iterate through each number as the first element of the triplet, and use a two-pointer 
approach (`left` and `right`) for the remaining portion of the array to find pairs that sum 
to the negative of the first element. Skip duplicate values for both the first element 
and the left pointer to avoid duplicate triplets in the result.

Examples:
- Input: nums = [-1, 0, 1, 2, -1, -4] -> Output: [[-1, -1, 2], [-1, 0, 1]]
- Input: nums = [0, 1, 1] -> Output: []

Complexity:
- Time: O(N^2) where N is the number of elements in the array, due to sorting and the nested two-pointer traversal.
- Space: O(N) auxiliary space required for Timsort.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = a + nums[left] + nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result
