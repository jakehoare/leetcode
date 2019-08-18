_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/parallel-courses/
# There are N courses, labelled from 1 to N.
# We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y:
# course X has to be studied before course Y.
# In one semester you can study any number of courses as long as you have studied all the prerequisites
# for the course you are studying.
# Return the minimum number of semesters needed to study all courses.
# If there is no way to study all the courses, return -1.

# Map each course to the list of next courses, and to a count of its prerequisites.
# Repeatedly take all courses with no prerequisites and decreases the prerequisite counts of all courses that they
# are prerequisites for. Update the courses that now have all their prerequisites taken.
# Time - O(m + n)
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        course_to_next = defaultdict(list)      # map course to list of next courses
        prerequisite_count = defaultdict(int)   # map course to count of prerequisites
        for pre, post in relations:
            course_to_next[pre].append(post)
            prerequisite_count[post] += 1

        # initilaize list of courses with no prerequisites
        no_preresquisites = [course for course in range(1, N + 1) if prerequisite_count[course] == 0]
        taken, semesters = 0, 0     # counts of courses take and semesters

        while no_preresquisites:    # some course has no prerequisites
            new_no_preresquisites = []
            for course in no_preresquisites:
                for next_course in course_to_next[course]:
                    prerequisite_count[next_course] -= 1    # take course, so decrease prerequisites of next
                    if prerequisite_count[next_course] == 0:
                        new_no_preresquisites.append(next_course)

            semesters += 1
            taken += len(no_preresquisites)
            if taken == N:
                return semesters
            no_preresquisites = new_no_preresquisites

        return -1
