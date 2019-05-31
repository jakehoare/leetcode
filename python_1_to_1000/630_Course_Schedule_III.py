_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/course-schedule-iii/
# There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed
# on dth day. A course should be taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
# Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that
# can be taken.

# Sort by increasing deadline time. If a set of courses can be done before a deadline, then they can be done
# consecutively from the start time without gaps.
# Given the total length of all courses than can be taken so far, the course with the next deadline can also be taken
# if it does not extend the total length beyond its deadline.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        total_length = 0
        taken_courses = []

        courses.sort(key=lambda c: c[1])  # sort by increasing end time

        for duration, end in courses:

            if total_length + duration <= end:  # can take this course
                total_length += duration
                heapq.heappush(taken_courses, -duration)

            elif -taken_courses[0] > duration:  # take this course instead of current longest
                neg_longest = heapq.heappushpop(taken_courses, -duration)
                total_length += neg_longest + duration

        return len(taken_courses)