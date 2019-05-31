_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/kill-process/
# Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
# Each process only has one parent process, but may have one or more children processes. This is just like a
# tree structure. Only one process has PPID that is 0, which means this process has no parent process.
# All the PIDs will be distinct positive integers.
# We use two list of integers to represent a list of processes, where the first list contains PID for each process
# and the second list contains the corresponding PPID.
# Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that
# will be killed in the end. You should assume that when a process is killed, all its children processes will be killed.
# No order is required for the final answer.

# Create a dictionary mapping processes to their children. DFS. Keep processes to be killed in a list. Pop process off
# list and add children.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        node_to_children = defaultdict(list)

        for node, parent in zip(pid, ppid):
            node_to_children[parent].append(node)

        killed, to_kill = [], [kill]

        while to_kill:
            process = to_kill.pop()
            killed.append(process)
            to_kill += node_to_children[process]

        return killed