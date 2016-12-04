/*
https://leetcode.com/problems/palindrome-linked-list/
Given a singly linked list, determine if it is a palindrome.

Find the middle node (if odd length) or first node of second half (if even length).  Reverse from this node onwards.
Compare nodes of resulting lists.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head==null || head.next==null)
            return true;

        ListNode fast = head;
        ListNode slow = head;
        while (fast!=null && fast.next!=null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode rev_head = null;
        ListNode next = null;
        while (slow!=null) {
            next = slow.next;
            slow.next = rev_head;
            rev_head = slow;
            slow = next;
        }

        while (rev_head!=null) {
            if (head.val != rev_head.val)
                return false;
            head = head.next;
            rev_head = rev_head.next;
        }
        return true;
    }
}
