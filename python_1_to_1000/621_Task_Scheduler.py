_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/task-scheduler/
# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
# represent different tasks.Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.
# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n
# intervals that CPU are doing different tasks or just be idle.
# You need to return the least number of intervals the CPU will take to finish all the given tasks.

# Find the most frequent task and calculate the time to complete all instances of this task as the wait between tasks
# (n + 1) times the number of waits (nb_tasks - 1). For each task with the same count as the most frequent, increment
# the finishing time. All less frequent tasks can be scheduled to fill the remaining idle time, or else they extend
# the finish time without any idle time.
# In other words, the only situation when the tasks cannot be completed without idle time is when the most frequent
# task(s) cannot be scheduled within the length of tasks.
# Time - O(n * m), nb tasks * nb types of task
# Space - O(m)

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks)
        max_count = max(counts.values())

        result = (max_count - 1) * (n + 1)  # n + 1 time between max_count tasks

        for count in counts.values():
            if count == max_count:          # each task pushes back finish time
                result += 1

        return max(result, len(tasks))      # other tasks fill idle time


