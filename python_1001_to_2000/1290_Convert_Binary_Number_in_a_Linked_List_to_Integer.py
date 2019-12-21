_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Iterate along the linked list.
# For each node, multiply the previous result by 2 (left bit shift) and add the bit from the current node.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = 0

        while head:
            result = result * 2 + head.val
            head = head.next

        return result
