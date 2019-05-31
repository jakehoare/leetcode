_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/linked-list-cycle/
# Given a linked list, determine if it has a cycle in it.

# Increment fast pointer by 2 nodes and slow pointer by 1 node per time step.  If loop, fast will catch up with slow
# else fast will reach end.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype:
        """
        fast, slow = head, head
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False