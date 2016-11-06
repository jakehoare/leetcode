_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-linked-list-ii/
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

# Find tail of non-reversed section, reverse nodes between m and n, link back between non-reversed sections.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pseudo = ListNode(None)     # create a new pseudo head
        pseudo.next = head
        node = pseudo
        n -= m                      # n = nb nodes to be reversed - 1

        while m > 1:                # find the tail of the first non-reversed section
            node = node.next
            m -= 1

        reversed_head = None
        next_reverse = node.next

        while n >= 0:               # add next_reverse in front of reversed_head
            tail = next_reverse.next
            next_reverse.next = reversed_head
            reversed_head = next_reverse
            next_reverse = tail
            n -= 1

        node.next.next = tail       # link tail of reversed section to second non-reversed section
        node.next = reversed_head   # link tail of the first non-reversed section to reversed section

        return pseudo.next