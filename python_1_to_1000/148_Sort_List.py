_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-list/
# Sort a linked list in O(n log n) time using constant space complexity.

# Base case is empty list or single node. Else recursively split list in half, sort halves and merge.
# Time - O(n log n)
# Space - O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast, slow, prev = head, head, None
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next

        prev.next = None
        one = self.sortList(head)
        two = self.sortList(slow)

        return self.merge(one, two)


    def merge(self, one, two):

        dummy = merged = ListNode(None)

        while one and two:

            if one.val <= two.val:
                merged.next = one
                one = one.next
            else:
                merged.next = two
                two = two.next
            merged = merged.next

        merged.next = one or two    # add remaining list

        return dummy.next