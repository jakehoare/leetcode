_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-triangle-number/
# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a triangle.

# Iterate over sides in order of decreasing length. With current side as longest of triangle, consider the range of
# all shorter sides. Set shortest_side and middle_side as the shortest and longest sides in this range. If shortest +
# middle <= longest then cannot make a triangle so increase shortest. If a triangle can be made, then all longer
# shortest sides can also make a triangle so increment count and decrement middle side.
# Time - O(n**2)
# Space - O(1)
# Alternatively, count sides by length. Try all possible combinations of side lengths in a triple loop. Count the
# number of ways that the sides can be chosen out of those available with a given length. O(n**3) but faster if
# many duplicate lengths.

from collections import Counter

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        triangles = 0

        for i, longest_side in enumerate(nums):
            left, right = 0, i - 1

            while left < right:
                shortest_side, middle_side = nums[left], nums[right]

                if shortest_side + middle_side > longest_side:  # equality is not a triangle
                    triangles += right - left  # current shortest and all longer up to middle can make triangles
                    right -= 1  # decrement middle_side
                else:
                    left += 1  # increment shortest_side

        return triangles


from math import factorial
class Solution2(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sides = Counter(nums)
        if 0 in sides:
            del sides[0]
        sides = list(sides.items())  # tuples of (side length, count)
        sides.sort()
        triangles = 0

        def binom(n, k):
            if k > n:
                return 0
            return factorial(n) // (factorial(n - k) * factorial(k))

        for i, (s1, c1) in enumerate(sides):
            for j, (s2, c2) in enumerate(sides[i:]):
                j2 = j + i
                for s3, c3 in sides[j2:]:
                    if s1 == s2 == s3:  # all sides same length
                        triangles += binom(c1, 3)
                    elif s1 == s2:      # shortest 2 sides are same lenght
                        if s1 + s2 > s3:
                            triangles += c3 * binom(c1, 2)
                    elif s2 == s3:      # longest sides are same length
                        triangles += c1 * binom(c2, 2)
                    else:   # all different lengths
                        if s1 + s2 > s3:
                            triangles += c1 * c2 * c3

        return triangles