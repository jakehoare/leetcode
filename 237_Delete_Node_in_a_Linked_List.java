/*
https://leetcode.com/problems/delete-node-in-a-linked-list/
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Copy value of next node then link to node aftre next and remove next node.
Time - O(1)
Space - O(1)
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;       // copy value of next node
        ListNode temp = node.next;      // save next node
        node.next = node.next.next;     // link node to node after next
        temp = null;                    // delete next node
    }
}