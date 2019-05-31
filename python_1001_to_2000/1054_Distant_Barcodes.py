_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distant-barcodes/
# In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
# Rearrange the barcodes so that no two adjacent barcodes are equal.
# You may return any answer, and it is guaranteed an answer exists.

# Count the number of each barcode then sort the counts from most to least frequent.
# Iterate along the sorted barcodes, updating the result for each barcode then moving 2 places to fill the even indices.
# When we reach the end of the result, move back to index 1 to fill the odd indices.
# Time - O(n log n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        n = len(barcodes)
        freq = Counter(barcodes)
        freq = sorted([(count, num) for num, count in freq.items()], reverse=True)

        result = [0] * n
        i = 0                       # next index of result to be updated

        for count, num in freq:     # from most to least frequent
            for _ in range(count):  # use all occurrences of num
                result[i] = num
                i += 2
                if i >= n:
                    i = 1

        return result
