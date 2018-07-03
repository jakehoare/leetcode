_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-rotation-with-highest-score/
# Given an array A, we may rotate it by a non-negative integer K so that the array becomes
# A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].
# Afterward, any entries that are less than or equal to their index are worth 1 point.
# Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.
# If there are multiple answers, return the smallest such index K.

# For each element of A, find the interval of rotation that cause the element to score a point. Increment rotations at
# index where first rotation occurs and at index after last rotation.
# Iterate over rotations calculating a running sum of the number of open intervals and find the max.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        rotations = [0 for _ in range(n)]

        for i, num in enumerate(A):

            min_rot = (i + 1) % n               # rotate element to end of array
            max_rot = (n - num + i + 1) % n     # rotate past index of num

            rotations[min_rot] += 1
            rotations[max_rot] -= 1
            if min_rot > max_rot:               # indices of rotation wrap around zero
                rotations[0] += 1

        score, max_score, best_rotation = 0, 0, 0

        for i, r in enumerate(rotations):
            score += r
            if score > max_score:
                max_score = score
                best_rotation = i

        return best_rotation