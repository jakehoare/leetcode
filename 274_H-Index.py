_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/h-index/
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute
# the researcher's h-index.   According to the definition of h-index on Wikipedia: "A scientist has index h if h of
# his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
# If there are several possible values for h, the maximum one is taken as the h-index.

# Bucket sort the papers by number of citations, using one bucket for all papers with len(citations) citations or
# more.  Starting from the bucket with the papers with the most citations, add those papers to the cumulative sum
# and until there are at least as many papers as citations.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        buckets = [0] * (len(citations)+1)      # each bucket index represents a number of citations
        for citation in citations:              # buckets[i] is the number of papers cited i times
            buckets[min(citation, len(citations))] += 1

        papers = 0                              # count of papers with at least buckets citations
        for bucket in range(len(buckets)-1, -1, -1):
            papers += buckets[bucket]
            if papers >= bucket:
                return bucket