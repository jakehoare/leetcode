_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a digit string, return all possible letter combinations that the number could represent.

# For each digit add all possible letter mappings to each of the previous results.
# Alternatively can be solved recursively.
# Time - O(n * 4^n)
# Space - O(n * 4^n), max 4 possible chars per digit so O(4^n) strings each of length n

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or '0' in digits or '1' in digits:
            return []

        results = [[]]
        mapping = {'2' : ['a', 'b', 'c'],
                   '3' : ['d', 'e', 'f'],
                   '4' : ['g', 'h', 'i'],
                   '5' : ['j', 'k', 'l'],
                   '6' : ['m', 'n', 'o'],
                   '7' : ['p', 'q', 'r', 's'],
                   '8' : ['t', 'u', 'v'],
                   '9' : ['w', 'x', 'y' , 'z']}

        for digit in digits:
            temp = []
            for result in results:
                for letter in mapping[digit]:
                    temp.append(result + [letter])
            results = temp

        # convert lists of chars to strings
        return ["".join(result) for result in results]