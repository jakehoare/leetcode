_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are
# connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the
# location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses
# all black pixels.

# If the black pixels are connected then every column and row in the enclosing rectangle contains a black pixel.  We
# search in each dimension separately for the first row/col with a black pixel and the first row/col after the (x,y)
# pixel without a black pixel.
# Time - O(mlogn + nlogm), binary search cols checking every row and vica versa
# Space - O(1)

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if not image or not image[0] or image[x][y] != '1':
            return 0

        # find lowest index of a row with any black cells
        top_edge = self.find_edge(0, x, True, True, image)

        # find lowest index of a row with any white cells
        bottom_edge = self.find_edge(x+1, len(image), True, False, image)

        # find lowest index of a col with any black cells
        left_edge = self.find_edge(0, y, False, True, image)

        # find lowest index of a col with any white cells
        right_edge = self.find_edge(y+1, len(image[0]), False, False, image)

        return (right_edge - left_edge) * (bottom_edge - top_edge)


    def find_edge(self, left, right, column, black, image):
        while left < right:
            mid = (left + right) // 2
            if black == self.any_black(mid, column, image):
                right = mid
            else:
                left = mid + 1
        return left


    def any_black(self, i, column, image):
        if column:      # if checking all columns, return True if any '1' in row i
            return ('1' in image[i])
        else:           # if checking all rows, return True if any '1' in column i
            return any(image[r][i] == '1' for r in range(len(image)))
