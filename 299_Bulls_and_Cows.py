_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bulls-and-cows/
# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to
# guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match
# the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and
# hints to eventually derive the secret number.
# For example: Secret number:  "1807" Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls
# and B to indicate the cows. In the above example, your function should return "1A3B".
# Please note that both secret number and friend's guess may contain duplicate digits.
# You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# Iterate over secret and guess together. If digits match increment bulls, else increment counts of unmatched digits in
# secret and guess. Then iterate over unmatched_guess digits, incrementing cows by the lower of unmatched_secret
# and unmatched_guess counts for each digit.
# Time - O(n)
# Space - O(1)

from collections import defaultdict

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        unmatched_secret, unmatched_guess = defaultdict(int), defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                unmatched_secret[s] += 1
                unmatched_guess[g] += 1

        for g, count in unmatched_guess.items():
            cows += min(unmatched_secret[g], count)

        return str(bulls) + "A" + str(cows) + "B"