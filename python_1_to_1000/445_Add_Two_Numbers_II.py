_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-two-numbers-ii/
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes
# first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Iterate over lists to calculate the integers they represent and sum them. Build resulting list from the least
# significant digit by repeatedly dividing by 10.
# Time - O(m + n)
# Space - O(max(m, n))

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0

        node = l1
        while node:
            num1 = num1 * 10 + node.val
            node = node.next
        node = l2
        while node:
            num2 = num2 * 10 + node.val
            node = node.next

        total = num1 + num2
        if total == 0:              # return single node with zero
            return ListNode(0)
        result = None

        while total:
            total, digit = divmod(total, 10)
            new_node = ListNode(digit)
            new_node.next = result  # make digit start of result
            result = new_node

        return result