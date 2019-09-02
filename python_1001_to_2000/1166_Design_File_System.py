_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-file-system/
# You are asked to design a file system which provides two functions:
# createPath(path, value): Creates a new path and associates a value to it if possible and returns True.
# Returns False if the path already exists or its parent path doesn't exist.
# get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
# The format of a path is one or more concatenated strings of the form:
# / followed by one or more lowercase English letters.
# For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.
# Implement the two functions.

# Build a tree of folders in the file system.
# Each node of the tree has a value and a map to child folders.
# To createPath, break the path into a list of folders and find the node of the penultimate folder. If the path is
# valid, insert the value in a new child node.
# To get, follow the folders down the tree, returning the final value if the path is valid.
# Time - O(n) for createPath and get where n is the number of previous createPath.
# Space - O(n)

class Node(object):
    def __init__(self, value):
        self.children = {}
        self.value = value

class FileSystem(object):

    def __init__(self):
        self.root = Node(None)

    # helper function, returns the last node from a path of folders or None
    def traverse(self, folders):
        node = self.root
        for folder in folders[1:]:
            if folder not in node.children:
                return None
            node = node.children[folder]
        return node

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        folders = path.split("/")
        node = self.traverse(folders[:-1])          # find the node of parent of last folder
        if node is None or folders[-1] in node.children:
            return False
        node.children[folders[-1]] = Node(value)    # insert the value
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        node = self.traverse(path.split("/"))
        if not node:
            return -1
        return node.value
