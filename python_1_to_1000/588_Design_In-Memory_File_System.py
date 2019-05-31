_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-in-memory-file-system/
# Design an in-memory file system to simulate the following functions:
# ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is
# a directory path, return the list of file and directory names in this directory. Your output (file and directory
# names together) should in lexicographic order.
# mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the
# middle directories in the path don't exist either, you should create them as well. This function has void return type.
# addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create
# that file containing given content. If the file already exists, you need to append given content to original content.
# This function has void return type.
# readContentFromFile: Given a file path, return its content in string format.

# Define a Folder as a mapping from names of files/folders to other Folders or None (for files). File system consists
# of root folder and mapping from file names to their contents. Separate file mapping speeds content retrieval/update.
# Time - O(1) for constructor. O(s + n + m log m) for ls where s = path number of chars, n = number of folders in
# path, m = number of results in final folder. O(s + n) for mkdir. O(s + n + t) for addContentToFile where t is
# total content. O(t) for readContentFromFile.
# Space - O(total nb folders + total content length)

class Folder(object):
    def __init__(self):
        self.children = {}      # map from child names to Folders or None


class FileSystem(object):
    def __init__(self):
        self.root = Folder()    # empty root folder
        self.files = {}         # map from file name to content

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        path = path.split("/")
        if path[-1] in self.files:
            return [path[-1]]       # list of single file

        folder = self.root
        if path[-1] != "":          # path of "/" is split to ["", ""]
            for folder_string in path[1:]:
                folder = folder.children[folder_string]
        return sorted(list(folder.children.keys()))         # sorted returns the list

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        folder = self.root
        for folder_string in path.split("/")[1:]:           # ignore first empty string
            if folder_string not in folder.children:        # make new folder
                folder.children[folder_string] = Folder()
            folder = folder.children[folder_string]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        path = filePath.split("/")
        file_name = path[-1]

        if file_name in self.files:
            self.files[file_name] += content

        else:
            self.files[file_name] = content
            folder = self.root
            for folder_string in path[1:-1]:
                folder = folder.children[folder_string]
            folder.children[file_name] = None

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        file_name = filePath.split("/")[-1]
        return self.files[file_name]