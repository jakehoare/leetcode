_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/exclusive-time-of-functions/
# Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive
# time of these functions.
# Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.
# A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0
# starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.
# Exclusive time of a function is defined as the time spent within this function, the time spent by calling other
# functions should not be considered as this function's exclusive time. You should return the exclusive time of each
# function sorted by their function id.

# When a function starts, if there is a current function already running then update the exclusive time and push
# current onto stack. Update new current function and time. Else if finish then update exclusive time of finished
# function (extra +1 because start is at perriod start and end is at end) and update current function and its restart
# time.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        exclusive = [0 for _ in range(n)]
        current, start = None, None

        for log in logs:
            fn, state, time = log.split(":")
            fn, time = int(fn), int(time)

            if state == "start":
                if current is not None:
                    exclusive[current] += time - start
                    stack.append(current)
                current, start = fn, time

            else:
                exclusive[current] += time - start + 1      # +1 because finish is at end of time step
                if stack:
                    current = stack.pop()
                    start = time + 1
                else:
                    current, start = None, None

        return exclusive

