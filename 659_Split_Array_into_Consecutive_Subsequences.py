_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into
# several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can
# make such a split.

# Count each num. For each num, reduce count and extend a sequence ending with num - 1 if possible. Otherwise use num
# and num + 1 and num + 2 to create a new sequence. Otherwise num cannot be used.
# Time - O(n)
# Space - O(n)

from collections import Counter, defaultdict

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = Counter(nums)
        sequences = defaultdict(int)  # map from num to number of sequences ending with num

        for num in nums:

            if freq[num] == 0:  # num already used to extend other sequences
                continue
            freq[num] -= 1

            if sequences[num - 1] != 0:  # extend an existing sequence
                sequences[num - 1] -= 1
                sequences[num] += 1

            elif freq[num + 1] > 0 and freq[num + 2] > 0:  # create a new sequence
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                sequences[num + 2] += 1

            else:  # cannot use num
                return False

        return True
