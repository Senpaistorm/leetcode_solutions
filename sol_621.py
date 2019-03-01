# 621. Task Scheduler
# Medium

# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

# Example:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

 

# Note:

#     The number of tasks is in the range [1, 10000].
#     The integer n is in the range [0, 100].
import collections

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        
        # sanitize the input with a dict/counter data structure
        count = collections.Counter(tasks)
        count = sorted(count.values(), reverse = True)
        # highest occurrence 
        nGap = count[0] - 1
        # total idle time
        idle = n * nGap
        # calculate occupied in idle and subtract it from idle
        # for every colomn of tasks A, B, ...
        for c in count[1:]:
            idle -= min(nGap, c)
        # if there is idle time, return idle + sum of all count
        # if there is no idle time and all tasks can be scheduled, return sum of all count
        return idle + sum(count) if idle > 0 else sum(count)

sol = Solution()

print(sol.leastInterval(["A","A","A","B","B","B"], 3))
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
print(sol.leastInterval(["A","A","A","B","B","B"], 1))

print(sol.leastInterval(["A","A","A","B","B","B"], 0))

                


