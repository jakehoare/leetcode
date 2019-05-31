_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/course-schedule-ii/
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1].  Given the total number of courses and a list of prerequisite pairs,
# return the ordering of courses you should take to finish all courses.   There may be multiple correct orders,
# you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# As per problem 207, find courses with no prerequisites and remove dependencies on such courses.
# Time - O(m + n)
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        nb_prerequisites = defaultdict(int)     # key is course, value is number of prerequisite courses
        prereq_list = defaultdict(list)         # key is a course, value is list of courses that depend on course

        for after, before in prerequisites:
            nb_prerequisites[after] += 1
            prereq_list[before].append(after)

        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())

        while can_take:

            course = can_take.pop()                     # take any course with no prerequisites
            order.append(course)
            for dependent in prereq_list[course]:
                nb_prerequisites[dependent] -= 1        # decrement count of dependencies
                if nb_prerequisites[dependent] == 0:    # no more prerequisites
                    can_take.add(dependent)

        return order if len(order) == numCourses else []