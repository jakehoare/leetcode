/*
https://leetcode.com/problems/meeting-rooms/
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

Define a comparator for Interval class such that they are sorted by start time.
If any interval starts before the previous interval has finished return false else return true.
Time - O(n log n) to sort
Space - O(1)
*/

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */


public class Solution {

    public static Comparator<Interval> intervalCompare = new Comparator<Interval>() {
        public int compare(Interval a, Interval b) {
            return a.start - b.start;
        }
    };

    public boolean canAttendMeetings(Interval[] intervals) {
        Arrays.sort(intervals, intervalCompare);
        for (int i = 1; i < intervals.length; ++i) {
            if (intervals[i].start < intervals[i-1].end)
                return false;
        }
        return true;
    }
}
