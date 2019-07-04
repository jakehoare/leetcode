_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/statistics-from-a-large-sample/
# We sampled integers between 0 and 255, and stored the results in an array count:
# count[k] is the number of integers we sampled equal to k.
# Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating point numbers.
# The mode is guaranteed to be unique.
# Recall that the median of a sample is:
# The middle element, if the elements of the sample were sorted and the number of elements is odd;
# The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.

# Iterate along count, updating the count of samples_seen.
# Find the index or indices of the median element(s).
# If 2 median elements, find their sum.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        minimum = None
        sample_count = sum(count)
        sum_samples, samples_seen = 0, 0
        mode, mode_count = 0, 0

        median_sum = 0
        median_indices = [sample_count // 2]
        if sample_count % 2 == 0:
            median_indices.append(median_indices[-1] - 1)

        for num, freq in enumerate(count):
            if freq == 0:
                continue

            if minimum is None:
                minimum = num
            maximum = num

            samples_seen += freq
            sum_samples += freq * num

            if freq > mode_count:
                mode_count = freq
                mode = num

            while median_indices and samples_seen > median_indices[-1]:
                median_sum += num
                median_indices.pop()

        mean = sum_samples / float(sample_count)
        median = median_sum / float(2 if sample_count % 2 == 0 else 1)
        return [minimum, maximum, mean, median, mode]
