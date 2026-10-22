"""
Idea:
Find the maximum area of water a container can store using a two-pointer approach. 
Initialize pointers at both ends of the array (`left` and `right`), compute the area using the width 
between pointers and the minimum of the two heights, and move the pointer corresponding to the shorter 
line inward to maximize potential area.

Examples:
- Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> Output: 49
- Input: height = [1, 1] -> Output: 1

Complexity:
- Time: O(N) where N is the number of elements in the height array, as the pointers traverse the array at most once.
- Space: O(1) auxiliary space.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            curr_height = min(height[l], height[r])
            max_area = max(max_area, width * curr_height)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
