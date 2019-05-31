_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-the-repetitions/
# Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".
# On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2
# such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not
# be obtained from “acbbe”.
# You are given two non-empty strings s1 and s2 and two integers n1 and n2. Now consider the strings S1 and S2,
# where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

# Step through s1, incrementing also in s2 if chars match. Go back to the beginning and increment reps at the end of
# either string. At end of s1, record position in s2 and reps. If position seen before then break because loop found.
# Find number of possible loops after initial stub. Add s2_reps for final stub.
# Time - O(m * n), iterate over s1 until have seen all ending positions in s2
# Space - O(m * n)

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if any(c for c in set(s2) if c not in set(s1)):     # early return if no result possible
            return 0

        i, j = 0, 0                                         # index counters in s1 and s2
        s1_reps, s2_reps = 0, 0                             # numbers of complete repetitions of s1 and s2 used
        s2_index_to_reps = {0 : (0, 0)}                     # map from j to (s1_reps, s2_reps)

        while s1_reps < n1:                                 # break if n1 copies of s1 used

            if s1[i] == s2[j]:
                j += 1                                      # increment j if chars match
            i += 1

            if j == len(s2):
                j = 0
                s2_reps += 1

            if i == len(s1):
                i = 0
                s1_reps += 1
                if j in s2_index_to_reps:                   # same position in s2 as before, in a loop
                    break
                s2_index_to_reps[j] = (s1_reps, s2_reps)    # record reps at this position in s2

        if s1_reps == n1:                                   # no loop found
            return s2_reps // n2

        initial_s1_reps, initial_s2_reps = s2_index_to_reps[j]
        loop_s1_reps = s1_reps - initial_s1_reps
        loop_s2_reps = s2_reps - initial_s2_reps
        loops = (n1 - initial_s1_reps) // loop_s1_reps      # number of loops possible after initial_s1_reps

        s1_reps = initial_s1_reps + loops * loop_s1_reps
        s2_reps = initial_s2_reps + loops * loop_s2_reps

        while s1_reps < n1:                                 # until n1 copies of s1 used

            if s1[i] == s2[j]:
                j += 1
            i += 1

            if i == len(s1):
                i = 0
                s1_reps += 1

            if j == len(s2):
                j = 0
                s2_reps += 1

        return s2_reps // n2
