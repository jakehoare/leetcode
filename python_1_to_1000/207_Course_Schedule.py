_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/course-schedule/
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Topological sort.  Find nodes with no dependencies.  Remove outgoing edges from each such node.  Repeat until
# no node has no dependencies.
# Time - O(m + n), edges + nodes
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nb_prerequisites = defaultdict(int)     # key is course, value is number of prerequisite courses
        prereq_list = defaultdict(list)         # key is a course, value is list of courses that depend on course

        for after, before in prerequisites:
            nb_prerequisites[after] += 1
            prereq_list[before].append(after)

        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())

        while can_take:

            course = can_take.pop()                     # take any course with no prerequisites
            numCourses -= 1                             # decrement count of remaining courses to be taken
            for dependent in prereq_list[course]:
                nb_prerequisites[dependent] -= 1        # decrement count of dependencies
                if nb_prerequisites[dependent] == 0:    # no more prerequisites
                    can_take.add(dependent)

        return numCourses == 0
