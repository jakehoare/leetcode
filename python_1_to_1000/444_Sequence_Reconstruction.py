_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sequence-reconstruction/
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence
# is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common
# supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences
# of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

# Note org is permutation hence no duplicates. Create set of all consecutive pair in org and mapping from each num in
# org to its index. For each seq remove any consecutive pair from pairs and check numbers appear in increasing index
# order in org. Consecutive pairs in some seq ensures there is no choise condition
# Time - O(s + n), total length of all seqs + org
# Space - O(n)

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        extended = [None] + org  # prepend with None to catch len(org) == 1
        pairs = set((n1, n2) for n1, n2 in zip(extended, org))
        num_to_index = {num: i for i, num in enumerate(extended)}

        for seq in seqs:

            for n1, n2 in zip([None] + seq, seq):

                if n2 not in num_to_index or num_to_index[n2] <= num_to_index[n1]:
                    return False
                last_index = num_to_index[n2]

                pairs.discard((n1, n2))

        return not pairs