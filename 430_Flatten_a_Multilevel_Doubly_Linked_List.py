_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# You are given a doubly linked list which in addition to the next and previous pointers,
# it could have a child pointer, which may or may not point to a separate doubly linked list.
# These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.
# Flatten the list so that all the nodes appear in a single-level, doubly linked list.
# You are given the head of the first level of the list.

# Iterate along the main list, inserting child lists. Ensure links are in both directions and remove links to
# children when flattened.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node = head                     # save the head to be returned

        while node:                     # iterate over the list

            if node.child:

                old_next = node.next    # save the next so we can link the tail of the flattened child list
                node.next = self.flatten(node.child)    # insert the flattened child list
                node.next.prev = node   # link child list back to node
                node.child = None       # remove the child since it is now flattened

                while node.next:
                    node = node.next    # find tail of child list
                node.next = old_next    # link tail to old_next
                if old_next:            # link in other direction
                    old_next.prev = node

            node = node.next            # move to the next node

        return head