_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/stamping-the-sequence/
# You want to form a target string of lowercase letters.
# At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.
# On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the
# corresponding letter from the stamp.  You can make up to 10 * target.length turns.
# For example, if the initial sequence is "?????", and your stamp is "abc",
# then you may make "abc??", "?abc?", "??abc" in the first turn.
# Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.
# If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped
# at each turn.  If the sequence is not possible to stamp, return an empty array.
# For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2],
# corresponding to the moves "?????" -> "abc??" -> "ababc".
# Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.
# Any answers specifying more than this number of moves will not be accepted.

# From given indices i of target and j of stamp, recursively attempt to build a solution.
# Base cases are too many stamps and having the reached end of the target.
# If at the end of the stamp, we can have put an earlier stamp which now shows only its suffix (may be the whole stamp).
# If stamp and target chars match, we can continue with next chars of stamp and target, or try to start a new stamp.
# Memoize results.
# Time - O(mn) since there are mn possible states and building results is O(1) due to max length of 10.
# Space - O(mn)

class Solution:
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        memo = {}

        def helper(i, j, results):          # stamp from target[i] and stamp[j] given list of partial results

            if (i, j) in memo:
                return memo[(i, j)]

            if len(results) > 10 * len(target): # too many stamps
                return []

            if i == len(target):            # end of target, check if end of stamp
                return results if j == len(stamp) else []

            if j == len(stamp):             # end of stamp
                for k in range(len(stamp)):
                    temp = helper(i, k, [i - k] + results)  # stamp before existing result so only suffix shows
                    if temp:
                        result = temp
                        break
                else:
                    result = []

            elif target[i] != stamp[j]:     # cannot continue current stamp
                result = []

            else:
                temp = helper(i + 1, j + 1, results)    # continue current stamp
                if temp:
                    result = temp
                else:                       # start a new stamp
                    result = helper(i + 1, 0, results + [i + 1])

            memo[(i, j)] = result
            return result

        return helper(0, 0, [0])

