/*
https://leetcode.com/problems/binary-watch/
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Enumerate all times (12 * 60 = 720 possibilities) and count number of with bits set equal to num.
Alternatively, precompute bits set for all times and look up.
Time - O(1) since finite number of times.
Space - O(1)
*/

public class Solution {
    public List<String> readBinaryWatch(int num) {

    List<String> times = new ArrayList<>();
    for (int hour = 0; hour < 12; ++hour) {
        for (int minute = 0; minute < 60; ++minute) {
            if (Integer.bitCount(hour) + Integer.bitCount(minute) == num)
                times.add(String.format("%d:%02d", hour, minute));
        }
    }
    return times;
    }
}