_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-absolute-file-path/
# Suppose we abstract our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents the directory dir contains an empty sub-directory
# subdir1 and a sub-directory subdir2 containing a file file.ext.
# Given a string representing the file system in the above format, return the length of the longest absolute path to
# file in the abstracted file system. If there is no file in the system, return 0.

# For each line, depth is number of prefix tabs.  If line cointains "." update longest with stripped line length +
# depth (for intervening "/") + depths[depth] (for directories).  Else if not a file, update the next directory
# length as directory length at this depth + new directory length.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        longest = 0
        depths = [0]    # depths[i] is the cumulative length of all directory strings preceeding file at depth i.

        for line in input.splitlines():

            stripped = line.lstrip("\t")
            depth = len(line) - len(stripped)

            if "." in line:
                longest = max(longest, len(stripped) + depth + depths[depth])
            else:
                if len(depths) <= depth + 1:
                    depths.append(0)
                depths[depth + 1] = depths[depth] + len(stripped)

        return longest