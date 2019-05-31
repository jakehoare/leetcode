_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/read-n-characters-given-read4/
# The API: int read4(char *buf) reads 4 characters at a time from a file.
# The return value is the actual number of characters read. Eg, it returns 3 if only 3 characters are left in the file.
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

# Read up to 4 chars into buf4 and copy to buf (which is modified in-place).
# Time - O(n)
# Space - O(n)

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

class Solution:
    def read(self, buf, n):

        total_chars, last_chars = 0, 4

        while last_chars == 4 and total_chars < n:

            buf4 = [""] * 4     # temporary buffer
            last_chars = min(read4(buf4), n - total_chars)
            buf[total_chars:total_chars+last_chars] = buf4
            total_chars += last_chars

        return total_chars