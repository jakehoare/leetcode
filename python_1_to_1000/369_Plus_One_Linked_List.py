_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/plus-one-linked-list/
# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# Add zero to the front then find the digit before the first 9.  Increment that digit and set all digits after to zero.
# remove leading zero if not incremented.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)      # make a new head with zero digit
        new_head.next = head
        i, j = new_head, new_head   # pointers

        while i.next:               # iterate along the list
            i = i.next
            if i.val != 9:          # update j to find the last node that is not 9
                j = i

        j.val += 1                  # increment j
        j = j.next
        while j:                    # set all after j to zero
            j.val = 0
            j = j.next

        if new_head.val == 0:       # not incremented new_head
            return head
        return new_head
