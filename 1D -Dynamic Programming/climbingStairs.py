"""
Idea:
Use dynamic programming with two variables (one and two) to track the number of ways 
to reach the current step. This is identical to the Fibonacci sequence, where each step 
is the sum of the previous two steps. Iterate from the bottom up to compute the result in linear time.

Examples:
- Input: n = 2 -> Output: 2 (1 + 1 = 2, 2 = 2)
- Input: n = 3 -> Output: 3 (1 + 1 + 1 = 3, 1 + 2 = 3, 2 + 1 = 3)
- Input: n = 5 -> Output: 8 (1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1)

Complexity:
- Time: O(N) since we iterate n - 1 times.
- Space: O(1) using only constant extra space for variables.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one
