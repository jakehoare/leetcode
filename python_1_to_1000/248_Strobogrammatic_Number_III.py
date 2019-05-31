_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/strobogrammatic-number-iii/
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
# Because the range might be a large number, the low and high numbers are represented as string.

# Build lists of numbers upto the length of high.  Wrap pairs of strobogrammatic digits around previous numbers.

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        max_len, min_len = len(high), len(low)
        low, high = int(low), int(high)

        live_list = ['']                # base case for even length numbers
        other_list = ['0', '1', '8']    # bas case for odd length numbers
        strobo_count = 0
        strobo = {'0' : '0', '1' : '1', '8': '8', '6' : '9', '9' : '6'}

        if min_len == 1:
            strobo_count += len([i for i in other_list if low <= int(i) <= high])

        for i in range(2, max_len+1):
            live_list = [c + r + strobo[c] for r in live_list for c in strobo]  # wrap c and strobo[c] around previous numbers

            if min_len < i < max_len:           # add all numbers in list not beginning with zero
                strobo_count += len([True for result in live_list if result[0] != '0'])
            elif i == min_len or i == max_len:  # add numbers not beginning with zero and between low and high
                strobo_count += len([True for result in live_list if result[0] != '0' and low <= int(result) <= high])

            live_list, other_list = other_list, live_list   # swap even and odd lists

        return strobo_count
