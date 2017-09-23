_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-concatenated-strings/
# Given a list of strings, you could concatenate these strings together into a loop, where for each string you could
# choose to reverse it or not. Among all the possible loops, you need to find the lexicographically biggest string
# after cutting the loop, which will make the looped string into a regular one.
# Specifically, to find the lexicographically biggest string, you need to experience two phases:
# Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
# Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.
# And your job is to find the lexicographically biggest one among all the possible regular strings.

# For each split point of each string and each reversed string, build the loop where each other string is oriented to
# its highest value.
# Time - O(n**2) for n total chars.
# Space - O(n)

class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = None
        best = [max(s, s[::-1]) for s in strs]

        for i, s in enumerate(strs):
            t = s[::-1]
            for j in range(len(s)):
                test = s[j:] + "".join(best[i + 1:] + best[:i]) + s[:j]
                test2 = t[j:] + "".join(best[i + 1:] + best[:i]) + t[:j]
                result = max(result, test, test2)

        return result