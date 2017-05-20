_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-unique-word-abbreviation/
# A string such as "word" contains the following abbreviations:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the
# smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.
# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.
# In the case of multiple answers, you may return any one of them.

# Encode each word in dictionary with same length as target, setting bits where word char != target char.
# For each possible pattern of chars in target to to retain, check if target differs from each word by at least one
# char. If so convert bitwise encoded trget to string and compare with shortest.
# Time - O(n * k * 2**n) where len(target) = n and len(dictionary) = k
# Space - O(kn)

class Solution(object):
    """
    :type target: str
    :type dictionary: List[str]
    :rtype: str
    """
    def minAbbreviation(self, target, dictionary):
        def abbr(target, num):
            word, count = [], 0  # count of char sequence that can be abbreviated
            for w in target:
                if num & 1 == 1:  # char in target must remain
                    if count:
                        word += str(count)
                        count = 0
                    word.append(w)
                else:  # char in target can be abbreviated
                    count += 1
                num >>= 1  # right shift, divide by 2

            if count:
                word.append(str(count))
            return "".join(word)

        m = len(target)
        diffs = []  # representation of each word in terms of which chars are different from target

        for word in dictionary:
            if len(word) != m:
                continue
            bits = 0
            for i, char in enumerate(word):
                if char != target[i]:  # set bits when chars are different
                    bits += 2 ** i
            diffs.append(bits)

        if not diffs:
            return str(m)

        min_abbr = target
        for i in range(2 ** m):  # i represents which chars remain in target
            if all(d & i for d in diffs):  # i has at least has one char different from every word in dictionary
                abbr_i = abbr(target, i)
                if len(abbr_i) < len(min_abbr):
                    min_abbr = abbr_i

        return min_abbr