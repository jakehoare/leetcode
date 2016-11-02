_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/simplify-path/
# Given an absolute path for a file (Unix-style), simplify it.

# Create result stack. Go up a level if '..'. Stay at same level if '.'.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')     # does not treat consecutive delimiters as one if delimiter specified
        result = []

        for item in path_list:
            if item == '..':            # go up one level if possible
                if result:
                    result.pop()
            elif item and item != '.':  # add item to path
                result.append(item)
            # else ignore '.' and ''

        return '/' + '/'.join(result)