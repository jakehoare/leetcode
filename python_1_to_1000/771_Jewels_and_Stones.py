_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/jewels-and-stones/
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
# so "a" is considered a different type of stone from "A".

# Check if each stone is in jewels. Generator saves creating a list.
# Time - O(m + n)
# Space - O(m)

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(1 for s in S if s in set(J))