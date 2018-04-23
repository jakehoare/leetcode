_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-watch/
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent
# the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times
# the watch could represent. The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid.

# Enumerate the possible arrangements of setting num bits. Set bits one at a time, initially the first bit can be in
# any position that allows enough space for the remaining bits. Then for each setting add the next bit in all positions
# that allow space for the remaining bits.

# For each setting, convert the first 4 bits to the hour and the last 6 to minutes. Reject if impossible. Format as
# time with zero padding for single-digit minutes.
# Time - O(n * 10! / n!(10 - n)!) 10 choose n possibilities, each of length n
# Space - O(n * 10! / n!(10 - n)!)

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]

        bits_set = [[i] for i in range(10)]         # list if times, each time is a list of which bits are set

        for max_bit in range(10 - num + 1, 10):     # allow space for other bits to be set

            new_bits_set = []

            for time in bits_set:
                for bit in range(time[-1] + 1, max_bit + 1):
                    new_bits_set.append(time + [bit])   # set all possible next bits

            bits_set = new_bits_set

        result = []

        for time in bits_set:

            hours, mins = 0, 0

            for bit in time:
                if bit >= 6:                        # hours bits
                    hours += 1 << (bit - 6)
                else:                               # minutes bits
                    mins += 1 << bit

            if hours < 12 and mins < 60:            # valid time

                mins = str(mins)
                if len(mins) == 1:                  # pad with leading zero
                    mins = "0" + mins
                result.append(str(hours) + ":" + mins)

        return result