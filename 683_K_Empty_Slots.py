_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-empty-slots/
# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days.
# In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the
# flower will open in that day.
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x
# will be in the range from 1 to N.
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and
# also the number of flowers between them is k and these flowers are not blooming.
# If there isn't such day, output -1.

# Convert to a list where indices represent positions and values represent days. Create a window with k intervening
# flowers and check if any bloom earlier than those at the ends. If so, then reset the window start to the earlier
# blooming flower, because flowers already visited bloom later and so cannot start a new window. Else if no flower
# blooms earlier than the window ends, update the earliest_day with the later of the flowers at the ends of the
# window and start a new window where the current window ends.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        days = [None for _ in range(n)]         # index is position and value is day of blooming
        for day, pos in enumerate(flowers, 1):  # index days from 1
            days[pos - 1] = day                 # positions indexed from 0

        left, right = 0, k + 1                  # indices in days of ends of window
        first_day = n + 1                       # first day with a gap of length k between 2 flowers

        while right < n:
            for i in range(left + 1, right):    # check all intervening flowers between ends of window
                if days[i] < days[left] or days[i] < days[right]:   # flower at i blooms earlier than ends
                    left, right = i, i + k + 1  # start new window with earlier blloming flower
                    break
            else:
                first_day = min(first_day, max(days[left], days[right]))    # no intervening bloom earlier
                left, right = right, right + k + 1  # start new window at end of this window

        return -1 if first_day == n + 1 else first_day

