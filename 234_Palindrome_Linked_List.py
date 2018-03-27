_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.

# Find the length of the list and move to the first node after the middle. Reverse right half of the list in-place.
# Iterate along original list and reversed right half, checking for equality of val.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node, length = head, 0
        while node:
            node = node.next
            length += 1

        if length < 2:
            return True

        node, i = head, 0
        while i < (length + 1) // 2:            # iterate to start of right-half (ignoring middle)
            node = node.next
            i += 1

        rev_head, rev_next = node, node.next    # rev_head is head of already reversed part
        rev_head.next = None                    # rev_next is head of part to be reversed

        while rev_next:
            temp = rev_next.next                # store what will be new rev_next
            rev_next.next = rev_head            # link rev_next to rev_head
            rev_head, rev_next = rev_next, temp

        while rev_head:
            if head.val != rev_head.val:        # check values are same
                return False
            head, rev_head = head.next, rev_head.next

        return True