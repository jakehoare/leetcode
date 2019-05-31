_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/expression-add-operators/
# Given a string that contains only digits 0-9 and a target value, return all possibilities to insert binary operators
# +, -, or * between the digits so they evaluate to the target value.

# Insert an operator (except before first digit) then for each partition of the remaining digits treat the first part
# as the next integer.  Track the evaluation of the current expression and the result of appending '*1' to the
# expression and so multiplying the last part by 1.
# Time - O(4**(n-1)), choice of 3 operators or none at each partition point.
# Space - O(n * 4**(n-1)), worst case input of all zeros

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        self.num, self.target, self.expressions = num, target, []
        self.helper("", 0, 0, 0)
        return self.expressions


    def helper(self, path, index, eval, multed):

        if index == len(self.num) and self.target == eval:
            self.expressions.append(path)

        for i in range(index, len(self.num)):   # use num[index:i+1] as next integer

            if i != index and self.num[index] == '0':
                break                           # no leading zeros unless single digit

            cur_str = self.num[index:i+1]       # insert operator then cur
            cur_int = int(cur_str)

            if index == 0:                      # no operator if start of nums
                self.helper(path + cur_str, i + 1, cur_int, cur_int)
            else:
                self.helper(path + "+" + cur_str, i + 1, eval + cur_int , cur_int)
                self.helper(path + "-" + cur_str, i + 1, eval - cur_int, -cur_int)
                self.helper(path + "*" + cur_str, i + 1, eval - multed + multed * cur_int, multed * cur_int)
