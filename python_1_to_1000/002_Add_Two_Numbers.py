_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-two-numbers/
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Iterate over lists. Add to result a node with the the sum of input nodes plus carry, mod 10.
# Time - O(max(m,n)) where m and n are input list lengths.
# Space - O(max(m,n)), output will be at most one digit more than longest input.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = result = ListNode(None)      # dummy head
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10

        return result.next