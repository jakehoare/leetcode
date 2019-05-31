_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/linked-list-components/
# We are given head, the head node of a linked list containing unique integer values.
# We are also given the list G, a subset of the values in the linked list.
# Return the number of connected components in G, where two values are connected if they appear consecutively in
# the linked list.

# Iterate over list, tracking whether the current node is or is not part of a connected component. Every time a new
# connected component starts, increment the count.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        H = set(G)              # convert to set for O(1) lookup

        count = 0
        connected = False       # is there a current connected component?

        while head:

            if head.val in H and not connected:     # start new connected component
                connected = True
                count += 1
            elif head.val not in G and connected:   # end existing connected component
                connected = False

            head = head.next

        return count