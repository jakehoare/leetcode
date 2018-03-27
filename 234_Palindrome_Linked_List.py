_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.

# Move a fast pointer and a slow pointer along the list. Slow pointer nodes are added to reversed list.
# When no more fast move is possible, iterate along slow and back along reversed list checking for val equality.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        rev = None                      # head of the already-reversed part

        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = rev
            rev = slow
            slow = next_slow

        # if fast is not null, slow is middle element of odd length list which is skipped
        # if fast is null, slow is first element of 2nd half of even length list
        if fast:
            slow = slow.next

        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next

        return True