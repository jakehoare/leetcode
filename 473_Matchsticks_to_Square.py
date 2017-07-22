_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/matchsticks-to-square/
# Your input will be several matchsticks, represented with their stick length. Your output will either be true or
# false, to represent whether you could make one square using all the matchsticks.

# Put each match in each side with capacity then recurse for next match.
# 3 heuristics to improve speed, 1) sort in descending order, 2) avoid duplicate recursive call, 3) pre-fill sides
# with exact matches
# Time - O(4**n)
# Space - O(1)

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(index):

            if index == len(nums):              # all sides are full
                return True

            for side in range(4):
                if sides[side] + nums[index] > target or sides[side] in sides[side + 1:]:   # match too long or
                    continue                    # skip if replicated side length to avoid duplicate recusrsion
                sides[side] += nums[index]      # add match to side
                if dfs(index + 1):
                    return True
                sides[side] -= nums[index]      # remove match if cannot fill all sides
            return False                        # match cannot fit on any side

        perimeter = sum(nums)
        target, remainder = divmod(perimeter, 4)
        if not perimeter or remainder:          # no matches or not divisible by 4
            return False

        nums.sort(reverse = True)               # fail early, e.g 5 matches are > target/2
        if nums[0] > target:                    # longest is greater than side length
            return False

        sides = [0] * 4                         # total length of matches on each side
        i = 0
        while i < 4 and nums[i] == target:      # prefill any side with matches of exact length
            sides[i] = target
            i += 1

        return dfs(i)
