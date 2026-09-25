"""
Idea:
Sort the meeting intervals by their start times. Iterate through the sorted intervals and 
check if the end time of the previous meeting is greater than the start time of the current meeting. 
If an overlap is found, return False. Otherwise, return True.

Examples:
- Input: intervals = [(0, 30), (5, 10), (15, 20)] -> Output: False
- Input: intervals = [(5, 8), (9, 15)] -> Output: True

Complexity:
- Time: O(N log N) due to sorting the intervals of length N.
- Space: O(1) or O(N) depending on the sorting implementation space overhead.
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval : interval.start)

        for i in range(1, len(intervals)):
            in1 = intervals[i-1]
            in2 = intervals[i]

            if in1.end > in2.start:
                return False

        return True
