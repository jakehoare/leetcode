_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
# Now we want to hire exactly K workers to form a paid group.
# When hiring a group of K workers, we must pay them according to the following rules:
# Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.

# Sort worker by increasing wage_per_quality. The cost of employing a group is the maximum wage_per_quality * sum of
# quality of the group. Form a group of the first K workers and find its total_quality and cost.
# Add each additional worker to the group, which increases the maximum wage_per_quality. Remove the worker with the
# highest quality, since they are most expensive to employ.
# Time - O(n logn)
# Space - O(n logn)

import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        wage_per_quality = [(w / float(q), q) for w, q in zip(wage, quality)]
        wage_per_quality.sort()

        workers = [-q for _, q in wage_per_quality[:K]]         # -qualities of workers in current group
        heapq.heapify(workers)
        total_quality = -sum(workers)
        cost = wage_per_quality[K - 1][0] * total_quality       # cost depends on highest wage_per_quality

        for wpq, q in wage_per_quality[K:]:
            heapq.heappush(workers, -q)
            total_quality += q + heapq.heappop(workers)         # remove worker with highest quality
            cost = min(cost, wpq * total_quality)

        return cost
