_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants
# represented by strings.
# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.

# Create a dictionary of the shorter list mapping restaurant to index. For each restaurant in the longer list, if it
# is in the dictionary then find the index sum. If there is a tie then append it to the result, if there is a new
# minimum then make it the lone result.
# Time - O(m + n)
# Space - O(min(m, n))

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if len(list1) > len(list2):         # swap to make list1 shorter
            list1, list2 = list2, list1

        dict1 = {rest: i for i, rest in enumerate(list1)}

        result = []
        min_sum = float("inf")

        for i, rest in enumerate(list2):

            if i > min_sum:                 # subsequent list2 entries cannot improve
                break

            if rest not in dict1:
                continue

            sum_i = i + dict1[rest]

            if sum_i < min_sum:             # new best
                min_sum = sum_i
                result = [rest]
            elif sum_i == min_sum:          # tie with current best
                result.append(rest)

        return result