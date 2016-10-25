_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.

# If there are at least k nodes, recursively reverse remainder and append reversed group to reversed remainder.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head

        node = head
        for _ in range(k):
            if not node:
                return head     # return head if there are not at least k nodes
            node = node.next
        # else node is now head of second group

        # reverse remainder after this group
        prev = self.reverseKGroup(node, k)

        for _ in range(k):      # reverse this group, adding in front of prev
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev