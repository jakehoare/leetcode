_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bold-words-in-string/
# Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between
# <b> and </b> tags become bold.
# The returned string should use the least number of tags possible, and of course the tags should form a
# valid combination.

# For each word, attempt to match with string. If match found, flag that matched chars should be bold then check again
# if word matches next starting position in S until word does not match S.
# Then iterate over S creating the result by inserting opening and closing tags amongst chars when flag changes to or
# from bold.
# Time - O(n * m) for S of length n and m chars in all words.
# Space - O(n)

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        S = "#" + S + "#"                       # add unused letter to avoid special cases for first and last chars
        bold = [False for _ in range(len(S))]   # flag which chars should be bold

        for word in words:
            i = S.find(word, 1)
            while i != -1:                      # while the word is found in S
                bold[i:i + len(word)] = [True] * len(word)      # set bold flags
                i = S.find(word, i + 1)         # search again for word in S from i + 1

        result = []

        for i in range(len(S)):

            if bold[i] and not bold[i - 1]:     # change from not bold to bold, opening tag
                result.append("<b>")
            elif not bold[i] and bold[i - 1]:   # change from bold to not vold, closing tag
                result.append("</b>")
            result.append(S[i])

        result = result[1:-1]                   # remove extra chars
        return "".join(result)