_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Write a program to find the node at which the intersection of two singly linked lists begins.
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.

# Traverse both lists, when reach end switch to start of other list.  If lists have l1 and l2 nodes before intersect
# and k nodes after then both traversals intersect after l1 + l2 + k nodes.  If no intersection, k = 0 and both pointers
# meet at None.
# Alternatively, count lengths and traverse longer list for length difference before traversing both in step.
# Time - O(n)
# Space - O(1)

import gc   # used to manually clear the memory

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        savedA, savedB = headA, headB

        while headA != headB:
            headA = savedB if not headA else headA.next
            headB = savedA if not headB else headB.next

        gc.collect()    # required to pass leetocde strict memory usage
        return headA


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        savedA, savedB = headA, headB
        len_diff = 0

        while headA.next:
            len_diff += 1
            headA = headA.next
        while headB.next:
            len_diff -= 1
            headB = headB.next

        if headA != headB:      # no intersection
            return

        headA, headB = savedA, savedB

        while len_diff != 0: # traverse longer list for length difference
            if len_diff > 0:
                headA = headA.next
                len_diff -= 1
            else:
                headB = headB.next
                len_diff += 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        gc.collect()
        return headA