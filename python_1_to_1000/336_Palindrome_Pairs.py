_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-pairs/
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation
# of the two words, i.e. words[i] + words[j] is a palindrome.

# Build a mapping from each word to its index in words.  Partition each word at ever possible point.  If left is a
# palindrome and reverse right is a word (but not the word itself), then add rev_right + word to the result.
# Repeat for right being a palindrome and rev_left a word.  Remove duplicates from words and their reverses by
# requiring left not to be empty.
# Time - O(n * k**2) where k is the max length of a word
# Space - O(n * k)

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        palindromes = []
        word_to_index = {}

        for i, word in enumerate(words):
            word_to_index[word] = i

        for i, word in enumerate(words):

            for first_right in range(len(word) + 1):

                left, right = word[:first_right], word[first_right:]
                rev_left, rev_right = left[::-1], right[::-1]

                if first_right != 0 and left == rev_left and rev_right in word_to_index and word_to_index[rev_right] != i:
                    palindromes.append([word_to_index[rev_right], i])

                if right == rev_right and rev_left in word_to_index and word_to_index[rev_left] != i:
                    palindromes.append([i, word_to_index[rev_left]])

        return palindromes
