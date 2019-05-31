_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/most-profit-assigning-work/
# We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job.
# Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete
# a job with difficulty at most worker[i].
# Every worker can be assigned at most one job, but one job can be completed multiple times.
# For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.
# If a worker cannot complete any job, his profit is $0.
# What is the most profit we can make?

# Zip the difficulties and profits together then sort to create a list of tuples with ascending difficulty.
# Sort the workers then iterate over workers. For each worker step through the list of jobs, updating best_profit for
# all jobs that this worker can do.
# Time - O(mlogm + nlogn) where len(difficulty) == m and len(worker) = n
# Space - O(m)

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        max_profits = list(zip(difficulty, profit))
        max_profits.sort()
        max_profits.append((float("inf"), 0))

        total_profit = 0
        best_profit = 0
        i = 0

        worker.sort()
        for diff in worker:

            while max_profits[i][0] <= diff:                        # all jobs worker can do
                best_profit = max(best_profit, max_profits[i][1])   # update best_profit
                i += 1
            total_profit += best_profit

        return total_profit