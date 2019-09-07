_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
# Let's define a function f(s) over a non-empty string s,
# which calculates the frequency of the smallest character in s.
# For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
# Now, given string arrays queries and words, return an integer array answer,
# where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

# Create a list to count the number of words with each f(word).
# Populate the list for each word, then iterate over the list in reverse order so it contains the cumulative count
# of words with the same or greater f(word).
# For each query, lookup f(query) + 1 in the cumulative frequency list, to return the number of words with a
# greater f(word).
# Time - O(m + n), the number of chars in words + the number of chars in queries
# Space - O(1), since words have at most 10 chars

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        word_freq = [0] * 12            # word_freq[i] is count of words with f(word) == i
        for word in words:
            word_freq[word.count(min(word))] += 1

        for i in range(10, 0, -1):      # update word_freq[i] to be the count of words with f(word) >= i
            word_freq[i] += word_freq[i + 1]

        # look up the count of words with f(word) > f(query)
        return [word_freq[query.count(min(query)) + 1] for query in queries]
