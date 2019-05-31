_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotate-list/
# Given a list, rotate the list to the right by k places, where k is non-negative.

# Count length of list, reset k to k % length (avoids repeated cycles).  Connect tail of list with head and then
# break k%length steps before the old tail.
# Time - O(n), n is length of list
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return

        count = 1
        node = head

        while node.next:
            node = node.next
            count += 1
        node.next = head        # connect tail to head

        to_move = count - (k % count)   #nb steps to move node before breaking
        while to_move > 0:
            node = node.next
            to_move -= 1
        head = node.next                # new head
        node.next = None

        return head