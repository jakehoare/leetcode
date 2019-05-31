_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/image-overlap/
# Two images A and B are given, represented as binary, square matrices of the same size
# A binary matrix has only 0s and 1s as values.
# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on
# top of the other image. After, the overlap of this translation is the number of positions that are 1 in both images.
# What is the largest possible overlap?

# Convert each 2-d image to a 1-d list of integers. Each integer represents a row, where setting the ith bit of the
# integer means the pixel at row[i] is set in the image.
# Then slide each image to all possible positions relative to the other image. For each overlapping row, right shift the
# integer representation of the slide row by the row shift, perform the logical AND with the static row and count the
# set bits.
# Time - O(n**3)
# Space - O(n)

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        def image_to_bits(image):       # convert each row to an integer
            bits = []
            for row in image:
                num = 0
                for i, bit in enumerate(reversed(row)):
                    if bit == 1:
                        num += (bit << i)
                bits.append(num)
            return bits

        A_bits, B_bits = image_to_bits(A), image_to_bits(B)
        rows, cols = len(A), len(A[0])
        max_overlap = 0

        for slide, static in ((A_bits, B_bits), (B_bits, A_bits)):  # keep one image static and slide the other
            for row_shift in range(rows):
                for col_shift in range(cols):

                    overlap = 0
                    for slide_row in range(rows - row_shift):       # the numebr of rows to slide
                        shifted = slide[slide_row] >> col_shift     # right shift the bits in this row
                        row_and = bin(shifted & static[slide_row + row_shift])  # AND with the static row
                        overlap += row_and.count("1")               # count the mutual set bits

                    max_overlap = max(max_overlap, overlap)

        return max_overlap