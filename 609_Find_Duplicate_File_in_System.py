_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-duplicate-file-in-system/
# Given a list of directory info including directory path, and all the files with contents in this directory, you
# need to find out all the groups of duplicate files in the file system in terms of their paths.
# A group of duplicate files consists of at least two files that have exactly the same content.
# A single directory info string in the input list has the following format:
#   "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
# It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content,
# respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just
# the root directory.
# The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files
# that have the same content. A file path is a string that has the following format:
#   "directory_path/file_name.txt"

# Create mapping of file content to its path (including file name).
# Time - O(n * k), number of paths * max path length
# Space - O(n * k)

from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_to_path = defaultdict(list)

        for path in paths:
            path_list = path.split(" ")     # path_list[0] is the path, other entries are files

            for f in path_list[1:]:
                open_bracket = f.index("(")
                close_bracket = f.index(")")
                content = f[open_bracket + 1:close_bracket]
                content_to_path[content].append(path_list[0] + "/" + f[:open_bracket])

        return [dup for dup in content_to_path.values() if len(dup) > 1]    # only return if at least 2 files
