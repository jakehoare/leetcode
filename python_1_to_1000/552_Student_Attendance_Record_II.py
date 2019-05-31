_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/student-attendance-record-ii/
# Given a positive integer n, return the number of all possible attendance records with length n, which will be
# regarded as rewardable. The answer may be very large, return it after mod 10**9 + 7.
# A student attendance record is a string that only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two
# continuous 'L' (late).

# Ignoring 'A', find the number of rewardable records for records of lengths up to n with dynamic programming. Modulo
# all additions. Final result is case of no 'A' or an 'A' in any position.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        BASE = 10 ** 9 + 7
        records = [1, 2]            # rewardable records of lengths 0 and 1
        zero, one, two = 1, 1, 0    # rewardable records ending in zero, one or two 'L'

        # new zero formed from previous zero, one and two + 'P'
        # new one formed form previous zero + 'L'
        # new two formed form previous one + 'L'
        for _ in range(2, n + 1):
            zero, one, two = (zero + one + two) % BASE, zero, one
            records.append((zero + one + two) % BASE)   # all possible numbers of 'L'

        # if A not present
        result = records[-1]

        # for each position of A
        for i in range(n):
            result += records[i] * records[n - 1 - i]   # records on LHS of 'A' * records on RHS
            result %= BASE

        return result