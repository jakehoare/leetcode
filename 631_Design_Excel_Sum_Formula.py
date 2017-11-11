_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-excel-sum-formula/
# Your task is to design the basic function of Excel and implement the function of sum formula. Specifically, you need
# to implement the following functions:
#  Excel(int H, char W): This is the constructor. The inputs represents the height and width of the Excel form.
# H is a positive integer, range from 1 to 26. It represents the height. W is a character range from 'A' to 'Z'.
# It represents that the width is the number of characters from 'A' to W. The Excel form content is represented by a
# height * width 2D integer array C, it should be initialized to zero. You should assume that the first row of C
# starts from 1, and the first column of C starts from 'A'.
#  void Set(int row, char column, int val): Change the value at C(row, column) to be val.
#  int Get(int row, char column): Return the value at C(row, column).
#  int Sum(int row, char column, List of Strings : numbers): This function calculate and set the value at C(row,
#      column), where the value should be the sum of cells represented by numbers. This function return the sum result
#      at C(row, column). This sum formula should exist until this cell is overlapped by another value or another
#      sum formula.
#      numbers is a list of strings that each string represent a cell or a range of cells. If the string represent a
#      single cell, then it has the following format : ColRow. For example, "F7" represents the cell at (7, F).
#      If the string represent a range of cells, then it has the following format : ColRow1:ColRow2. The range will
#      always be a rectangle, and ColRow1 represent the position of the top-left cell, and ColRow2 represents the
#      position of the bottom-right cell.

# Convert excel cell format to indices. Cells store integer or list of sum ranges. To sum, recurse on each cell in
# range until a value is found.
# Time - O(m * n) for init, get and sum. O(1) for set.
# Alternatively, store sum results in cells and use pointers from dependents to update sums on set().
# Space - O(m * n)

class Excel(object):
    def _indices(self, r, c):  # convert excel format to indices
        return [r - 1, ord(c) - ord("A")]

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        rows, cols = self._indices(H, W)
        self.excel = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        r, c, = self._indices(r, c)
        self.excel[r][c] = v

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        r, c = self._indices(r, c)
        return self.get_i(r, c)  # call get_i with indices

    def get_i(self, r, c):      # uses indices instead of excel format
        """
        :type r: int
        :type c: int
        :rtype: int
        """
        contents = self.excel[r][c]
        if isinstance(contents, int):  # base case of integer
            return contents

        total = 0
        for cells in contents:
            cell_range = cells.split(":")
            r1, c1 = self._indices(int(cell_range[0][1:]), cell_range[0][0])

            if len(cell_range) == 1:  # single cell
                r2, c2 = r1, c1
            else:  # range
                r2, c2 = self._indices(int(cell_range[1][1:]), cell_range[1][0])

            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    total += self.get_i(row, col)  # recurse, get_i with indices

        return total

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        r, c = self._indices(r, c)
        self.excel[r][c] = strs
        return self.get_i(r, c)  # call get_i with indices