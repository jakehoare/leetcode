_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-boxes/
# Given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous
# boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.

# Dynamic programming. Consider subarray from boxes[left:right+1] with same boxes of same colour as boxes[right] in a
# continuous subarray to the right of boxes[right]. Best score is either a) removing right and all same boxes, then
# best score form remaining subarray with no same, or b) is any box in subarray is same as boxes[right] then get best
# score from the subarray between this box and right, plus best score from left part of bubarray with same + 1.
# Time - O(n**3)
# Space - O(n**3)

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """

        def helper(left, right, same):  # same is number of boxes to right of boxes[right] that are same colour

            if left > right:
                return 0

            if (left, right, same) in memo:
                return memo[(left, right, same)]

            # extend same to left of boxes[right] as far as possible
            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                same += 1

            result = helper(left, right - 1, 0) + (same + 1) ** 2  # remove boxes[right] and same

            for i in range(left, right):    # if anx box i from left to right-1 is same as same then
                                            # remove boxes between i and right, then remove left to i with extended same
                if boxes[i] == boxes[right]:
                    result = max(result, helper(i + 1, right - 1, 0) + helper(left, i, same + 1))

            memo[(left, right, same)] = result
            return result

        memo = {}
        return helper(0, len(boxes) - 1, 0)