_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
# The API: int read4(char *buf) reads 4 characters at a time from a file.
# The return value is the actual number of characters read.
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# The read function may be called multiple times.

# Use a double-linked list to store any characters read by read4 but not required.  Use those characters first
# on the next call of read().
# Time - O(n)
# Space - O(n)

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

from collections import deque

class Solution(object):
    def __init__(self):
        self.leftover = deque()     # store chars read by read4 but not added previous buf

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total_chars, added_chars, read_chars = 0, 4, 0

        while self.leftover and total_chars < n:        # add leftover chars to buf
            buf[total_chars] = self.leftover.popleft()
            total_chars += 1

        while added_chars == 4 and total_chars < n:     # add blocks of 4 chars up to eof
            buf4 = [""] * 4     # temporary buffer
            read_chars = read4(buf4)
            added_chars = min(read_chars, n - total_chars)
            buf[total_chars:total_chars+added_chars] = buf4
            total_chars += added_chars

        while read_chars > added_chars:                 # save extra chars
            self.leftover.append(buf4[added_chars])
            added_chars += 1

        return total_chars