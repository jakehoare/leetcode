/*
https://leetcode.com/problems/student-attendance-record-i/
You are given a string representing an attendance record for a student. The record only contains the following
three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two
continuous 'L' (late). Return whether the student could be rewarded according to his attendance record.

Regular expression matching.
Time - O(n)
Space - O(1)
*/

class Solution {
    public boolean checkRecord(String s) {
        // .*A.*A.* means any char zero or more times before, between and after two As
        // .*LLL.* means any char before and after "LLL"
        return !s.matches(".*A.*A.*|.*LLL.*");

    }
}