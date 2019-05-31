_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/push-dominoes/
# There are N dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling
# or already fallen domino.
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left;
# S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# Return a string representing the final state.

# Iterate over dominos from right to left, for each domino finding the closest "R" that reach this domino. Repeat for
# closest "L" and iterating left to right. Then each domino that has not fallen falls according to whether an "R" or
# "L" that can impact it is closer.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def pushDominoes(self, dominos):
        """
        :type dominos: str
        :rtype: str
        """
        prev_R = float("-inf")              # current index of previous "R"
        rights = []                         # indices of previous "R" on the left of each domino
        for i, c in enumerate(dominos):
            rights.append(prev_R)
            if c == "R":                    # new prev_R
                prev_R = i
            elif c == "L":                  # no "R" can reach this domino
                prev_R = float("-inf")

        prev_L = float("inf")               # current index of previous "L"
        lefts = [0] * len(dominos)          # indices of previous "L" on the right of each domino
        for i in range(len(dominos) - 1, -1, -1):
            lefts[i] = prev_L
            if dominos[i] == "L":           # new prev_L
                prev_L = i
            elif dominos[i] == "R":         # no "L" can reach this domino
                prev_L = float("inf")

        dominos = [c for c in dominos]
        for i in range(len(dominos)):
            if dominos[i] == ".":           # not fallen already
                diff = (lefts[i] - i) - (i - rights[i]) # closest falling domino, negative for left, pos for right
                if diff < 0:
                    dominos[i] = "L"
                elif diff > 0:
                    dominos[i] = "R"

        return "".join(dominos)