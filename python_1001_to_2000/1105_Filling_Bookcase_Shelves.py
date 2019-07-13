_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/filling-bookcase-shelves/
# We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].
# We want to place these books in order onto bookcase shelves that have total width shelf_width.
# We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width),
# then build another level of shelf of the bookcase so that the total height of the bookcase has increased by
# the maximum height of the books we just put down.
# We repeat this process until there are no more books to place.
# Note again that at each step of the above process,
# the order of the books we place is the same order as the given sequence of books.
# For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf,
# the third book on the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

# Dynamic programming. Find the result for all books up to and including each book.
# For each end book, make a new shelf and repeatedly add books to that shelf until it has no remaining width.
# While the next book to be moved fits on the shelf, decrease the remaining width and update the height on the shelf.
# Update the total height result with the latest shelf + result up to the last book not moved.

# Time - O(n**2), since we may need to look at all previous books for each book.
# Space - O(n)

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        results = [0]                   # no height for no books

        for i in range(len(books)):
            width = shelf_width         # last shelf has no books initially
            shelf_height = 0
            results.append(float("inf"))
            j = i                       # index of next book to be moved to last shelf

            while j >= 0 and width >= books[j][0]:
                shelf_height = max(shelf_height, books[j][1])
                width -= books[j][0]
                results[-1] = min(results[-1], shelf_height + results[j])
                j -= 1

        return results[-1]

