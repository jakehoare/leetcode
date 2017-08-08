_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/teemo-attacking/
# In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition.
# Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's
# attacking, you need to output the total time that Ashe is in poisoned condition.
# You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

# For each time step, add min of the step and duration.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poisoned = 0
        timeSeries.append(float("inf"))
        for i in range(1, len(timeSeries)):
            poisoned += min(duration, timeSeries[i] - timeSeries[i- 1])
        return poisoned