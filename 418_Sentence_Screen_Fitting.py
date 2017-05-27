_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sentence-screen-fitting/
# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given
# sentence can be fitted on the screen.
# A word cannot be split into two lines.
# Two consecutive words in a line must be separated by a single space.

# Preprocess to find the number of complete sentences and the index of next starting word, for a row starting
# with each word. Fill row with complete sentences, then fill word by word. For each row find number of
# sentences and next starting word.
# Time - O(nc + r) where n is number of words, c is cols, r is rows.
# Space - O(n)

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        sentence_len = sum(len(w) for w in sentence) + len(sentence)

        # line_fits[i] = (number of complete sentences, index of next starting word) for a row starting with sentences[i]
        line_fits = []

        for start_word_index in range(len(sentence)):

            row_length, sentences = 0, 0
            word_index = start_word_index

            while row_length + sentence_len <= cols:  # can fit next sentence in row
                row_length += sentence_len
                sentences += 1

            while row_length + len(sentence[word_index]) <= cols:  # can fit next word in row
                row_length += len(sentence[word_index]) + 1  # extend row_length by word and space
                word_index += 1  # move to next word
                if word_index == len(sentence):  # fitted last word of sentence
                    sentences += 1
                    word_index = 0

            line_fits.append((sentences, word_index))

        fits, word_index = 0, 0
        for r in range(rows):
            sentences, next_word_index = line_fits[word_index]
            fits += sentences
            word_index = next_word_index

        return fits