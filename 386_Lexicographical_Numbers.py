_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lexicographical-numbers/
# Given an integer n, return 1 - n in lexicographical order.

# Next lexical num is previous * 10 if less than n.
# Else divide by 10 and increment until less than n, rhen remove all zeros.
# Alternatively, enumerate list id strings, sort and convert back to ints.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lexical = [1]

        while len(lexical) < n:

            num = lexical[-1] * 10
            while num > n:      # increment the smallest digit possible
                num //= 10
                num += 1
                while num % 10 == 0:    # strip off zeros
                    num //= 10
            lexical.append(num)

        return lexical

class Solution2(object):
    def lexicalOrder(self, n):
        strings = list(map(str, range(1, n + 1)))
        strings.sort()
        return list(map(int, strings))
