_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/loud-and-rich/
# In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money,
# and different levels of quietness.
# For convenience, we'll call the person with label x, simply "person x".
# We'll say that richer[i] = [x, y] if person x definitely has more money than person y.
# Note that richer may only be a subset of valid observations.
# Also, we'll say quiet[x] = q if person x has quietness q.
# Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest
# value of quiet[y]), among all people who definitely have equal to or more money than person x.

# Create graph mapping people to richer people. For each person, depth-first search the graph, first updating the
# results of all richer people, then if any richer people have a quieter result, update the result of the person.
# Time - O(m + n), number of richer relationships + number of people
# Space - O(m + n)

class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        richer_than = [set() for _ in range(n)]     # map person to richer people

        for a, b in richer:
            richer_than[b].add(a)

        result = [None] * n

        def update_results(person):

            if result[person] is not None:          # already found result
                return

            result[person] = person                 # default to self

            for rich in richer_than[person]:
                update_results(rich)                # update the results for richer people
                if quiet[result[rich]] < quiet[result[person]]: # if quiet is lower for result of richer ...
                    result[person] = result[rich]   # ... then result of this person is result of richer person

        for i in range(n):
            update_results(i)

        return result
