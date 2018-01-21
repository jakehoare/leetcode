_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-linked-list-in-parts/
# Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive
# linked list "parts".
# The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.
# This may lead to some parts being null.
# The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a
# size greater than or equal parts occurring later.
# Return a List of ListNode's representing the linked list parts that are formed.
# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

# Count length and calculate part lengths. Each part is previous root, count required nodes then break link to
# next part.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node, count = root, 0
        while node:                 # find length of linked list
            count += 1
            node = node.next

        part_length, odd_parts = divmod(count, k)
        result = []
        prev, node = None, root

        for _ in range(k):

            required = part_length  # required length of this part
            if odd_parts > 0:
                odd_parts -= 1
                required += 1

            result.append(node)
            for _ in range(required):
                prev, node = node, node.next
            if prev:                # break link to next part
                prev.next = None

        return result
