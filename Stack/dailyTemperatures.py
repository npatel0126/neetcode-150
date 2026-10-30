"""
Idea:
Find the number of days you have to wait until a warmer temperature for each day using a monotonic decreasing stack. 
Iterate through the temperatures while maintaining a stack of indices and their corresponding temperature values. 
Whenever the current temperature is strictly greater than the temperature at the top of the stack, pop from the stack 
and record the difference in indices as the number of days waited.

Examples:
- Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73] -> Output: [1, 1, 4, 2, 1, 1, 0, 0]
- Input: temperatures = [30, 40, 50, 60] -> Output: [1, 1, 1, 0]

Complexity:
- Time: O(N) where N is the number of temperatures, since each index is pushed and popped from the stack at most once.
- Space: O(N) to store the stack and result array.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # stores [temperature, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append([temp, i])
            
        return result
