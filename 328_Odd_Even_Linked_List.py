_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/odd-even-linked-list/
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

# Create 2 new dummy heads for odd and even index nodes.  Connect each pair of nodes to the odd and even lists
# respectively.  Break if no even node or next odd node.  Connect the odd and even lists.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)

        while head:
            odd.next = head         # append head to odd list
            odd = odd.next          # update head of odd list
            even.next = head.next   # append head.next to even list
            even = even.next        # update head of even list

            head = head.next.next if even else None # will break if no even or no even.next

        odd.next = even_head.next   # join lists, break link from last odd to last even
        return odd_head.next