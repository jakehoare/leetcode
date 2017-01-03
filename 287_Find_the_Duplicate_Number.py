_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-duplicate-number/
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# assume that there is only one duplicate number, find the duplicate one.
# You must not modify the array (assume the array is read only).
# There is only one duplicate number in the array, but it could be repeated more than once.

# For each integer i in nums, nums[i] is also in nums.  Since there are more slots in nums than unique integers in
# the range [1 .. n] inclusive then some integer must be duplicated.  By following a path i, nums[i], nums[nums[i]], ...
# the path must eventually repeat.  There is a cycle whereby nums[j] has already been visited.  Find cycle as per
# problem 142_Linked_List_Cycle_II - advance fast and slow pointers until they meet then reset one pointer to starting
# position and advance together until meet again.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[slow]

        while fast != slow:     # move slow pointer 1 step and fast 2 steps until collide
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0    # restart fast from index zero and move both pointers one step at a time
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast

