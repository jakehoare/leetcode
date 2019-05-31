_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/next-closest-time/
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9"
# are all invalid.

# Iterate over time from least significant digit. Attempt to increase each digit by looking for the smallest greater
# digit. Maximum allowed digit depends on index in time. If an increase is possible, make it and return. Else try
# again with next digit.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        result = [c for c in time]
        digits = set(int(c) for c in time[:2] + time[3:])       # set of digits in time
        min_digit = min(digits)
        max_digits = {0 : 2, 3 : 5, 4 : 9}                      # max possible digit at each index

        def increase(i):
            if i == 1:                                          # max digit depends on time[0]
                if time[0] == "2":
                    max_digit = 3
                else:
                    max_digit = 9
            else:
                max_digit = max_digits[i]

            larger_digits = [d for d in digits if int(time[i]) < d <= max_digit]
            return min(larger_digits) if larger_digits else -1

        for i in [4, 3, 1, 0]:                                  # iterate backwards, ignoring ":"
            increaseed = increase(i)
            if increaseed != -1:
                result[i] = str(increaseed)
                break
            else:
                result[i] = str(min_digit)

        return "".join(result)
