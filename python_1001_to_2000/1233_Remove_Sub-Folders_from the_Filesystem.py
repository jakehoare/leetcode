_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.
# If a folder[i] is located within another folder[j], it is called a sub-folder of it.
# The format of a path is one or more concatenated strings of the form:
# / followed by one or more lowercase English letters.
# For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

# Insert the paths in a trie in order of increasing length.
# Signify the terminal node when a path is fully inserted.
# If a path reaches a node that is already terminal, it is a subfolder.
# Time - O(n log n) for n folders.
# Space - O(n)

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        paths = [f.split("/") for f in folder]
        paths.sort(key=len)
        result = []
        root = {}

        for i, path in enumerate(paths):

            node = root
            for level in path[1:]:      # path[0] is empty due to leading "/"
                if level not in node:   # make a new node
                    node[level] = {}
                node = node[level]
                if "TERMINAL" in node:  # subfolder, do not add to result
                    break
            else:
                node["TERMINAL"] = {}
                result.append("/".join(path))

        return result
