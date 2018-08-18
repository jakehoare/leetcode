_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/guess-the-word/
# This problem is an interactive problem new to the LeetCode platform.
# We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.
# You may call master.guess(word) to guess a word.
# The guessed word should have type string and must be from the original list with 6 lowercase letters.
# This function returns an integer type, representing the number of exact matches (value and position) of your guess
# to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.
# For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10
# or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.
# Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.
# The letters of each word in those testcases were chosen independently at random from 'a' to 'z',
# such that every word in the given word lists is unique.

# Repeatedly choose a word to guess and eliminate all words that do not have the same number of matches as the
# chosen word. Words are chosen so they have maximum overlap (same chars in same positions) with other words.
# This reduces candidate list more than choosing a random word which may not overlap with any other words and so
# does not allow any other words to be eliminated.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def pair_matches(a, b):         # count the number of matching characters
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [[0 for _ in range(26)] for _ in range(6)]     # counts[i][j] is nb of words with char j at index i
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1

            best_score = 0
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord("a")]           # all words with same chars in same positions
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = wordlist[:]        # all remaining candidates, initially all words
        while candidates:

            s = most_overlap_word()     # guess the word that overlaps with most others
            matches = master.guess(s)

            if matches == 6:
                return

            candidates = [w for w in candidates if pair_matches(s, w) == matches]   # filter words with same matches