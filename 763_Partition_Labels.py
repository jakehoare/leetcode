_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-labels/
# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
# each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Map each character to its last index in S. Iterate over S, for each character update the end of the partition to be
# the later of current end and last appearance of the character. If we reach the end of the partition, add it to
# result and start new partition at next index.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        result = []

        start, end = 0, 0           # current partition
        for i, c in enumerate(S):

            end = max(end, last[c])
            if i == end:            # last appearance of all charcters in partition
                result.append(end - start + 1)
                start = i + 1       # start new partition. end will be updated on next iteration.

        return result