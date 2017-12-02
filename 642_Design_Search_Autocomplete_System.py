_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-search-autocomplete-system/
# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with
# a special character '#'). For each character they type except '#', you need to return the top 3 historical hot
# sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:
#  The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#  The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several
#   sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
#  If less than 3 hot sentences exist, then just return as many as you can.
#  When the input is a special character, it means the sentence ends, and in this case, you need to return
#   an empty list.
# Your job is to implement the following functions:
#  The constructor function:
#  AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data.
#   Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence
#   has been typed. Your system should record these historical data.
#  Now, the user wants to input a new sentence. The following function will provide the next character the user types:
#  List<String> input(char c): The input c is the next character typed by the user. The character will only be
#   lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed
#   sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix
#   the same as the part of sentence already typed.

# Store sentences that have already been seen in a map (key = sentence, value = count).
# When the first char of a new sentence is input, create a list of all previously seen sentences that match the first
# char, sorted by decreasing count. Then for each subsequent char, all we need to do is filter the existing list,
# keeping only sentences that match the char in its correct position.
# At the end of the input, simply increment the count.
# Time - O(n) for constructor when n is number of sentences. O(n log n) to input first char then O(n).
# Space - O(n)

from collections import defaultdict

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.partial = []  # previously seen chars of current sentence
        self.matches = []  # matching sentences in decreasing frequency order

        self.counts = defaultdict(int)  # map from sentence to its frequency
        for sentence, count in zip(sentences, times):
            self.counts[sentence] = count

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            sentence = "".join(self.partial)
            self.counts[sentence] += 1
            self.partial = []  # reset partial and matches
            self.matches = []
            return []

        if not self.partial:  # first char of sentence
            self.matches = [(-count, sentence) for sentence, count in self.counts.items() if sentence[0] == c]
            self.matches.sort()
            self.matches = [sentence for _, sentence in self.matches]  # drop the counts
        else:
            i = len(self.partial)  # filter matches for c
            self.matches = [sentence for sentence in self.matches if len(sentence) > i and sentence[i] == c]

        self.partial.append(c)
        return self.matches[:3]
