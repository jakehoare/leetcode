_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/middle-of-the-linked-list/
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Move fast pointer for 2 steps and slow pointer for 1 step until fast does not have a next next.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow