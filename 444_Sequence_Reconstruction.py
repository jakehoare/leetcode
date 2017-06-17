
from collections import defaultdict

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        return org == self.can_reconstruct(seqs, [0] * len(seqs), [])

    def can_reconstruct(self, seqs, pointers, reconstruction):

        int_to_seqs = defaultdict(set)  # value is set of all seqs indices where next integer is key
        for i, seq in enumerate(seqs):
            if pointers[i] < len(seq):
                int_to_seqs[seqs[i][pointers[i]]].add(i)

        if not int_to_seqs:
            return reconstruction

        reconstruct = set()
        saved_pointers = pointers[:]

        for num in int_to_seqs:
            for i in int_to_seqs[num]:
                pointers[i] += 1
            reconstruct.add(tuple(self.can_reconstruct(seqs, pointers, reconstruction + [num])))
            pointers = saved_pointers

        if len(reconstruct) != 1:
            return []
        return list(reconstruct.pop())

sol = Solution()
target = [1,2,3]
test =[[1,2],[1,3],[2,3]]
print(sol.sequenceReconstruction(target, test))