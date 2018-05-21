_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/student-attendance-record-i/
# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than
# two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance record.

# Find the count of 'A' and whether 'LLL' appears in s.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A") < 2 and "LLL" not in s