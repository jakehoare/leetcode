_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/divide-two-integers/
# Divide two integers without using multiplication, division and mod operator.
# If overflow, return MAX_INT.

# TODO SOLUTION
# Time - O(TODO)
# Space - O(1)

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        diff_sign = (divisor < 0) ^ (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            local_divisor = divisor
            local_count = 1

            while dividend >= local_divisor:
                dividend -= local_divisor
                result += local_count
                local_divisor <<= 1
                local_count <<= 1

        if diff_sign:
           result = -result
        return max(min(result, 2**31-1), -2**31)

if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(426, 7))