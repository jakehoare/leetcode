_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Whilst there are nodes in both lists, link to lowest head node and increment that list.  Finally link to
# the list with remaining nodes.
# Time - O(m+n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):

        prev = dummy = ListNode(None)       # new dummy head for the merged list

        while l1 and l2:                    # link prev to the lowest node

            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2                # link prev to the list with remaining nodes
        return dummy.next

