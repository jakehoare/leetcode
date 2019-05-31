_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/linked-list-cycle-ii/
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# If there are k nodes before a cycle of c nodes, when slow reaches start of loop, fast is k % c into loop.
# When fast reaches slow, both are c - k % c into the loop.  Restart fast at head and move both 1 step at a time.
# After k steps, both are at start of loop.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:

                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow

        return None
