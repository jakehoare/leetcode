_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/couples-holding-hands/
# N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so
# that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and
# switch seats.
# The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first
# couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
# The couples' initial seating is given by row[i] being the value of the person who is initially sitting in i-th seat.

# Create an undirected graph where nodes are seats (holding 2 people) and edges are links to the seats of the partners
# of the people on the seat. Each node has 2 undirected edges. Walk the graph until a cycle of length k is found. It
# then takes k - 1 swaps so put couples together.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row) // 2   # number of couples

        couple_to_location = [[] for _ in range(n)]     # map a couple index to current seating indices of the couple
        for i, person in enumerate(row):                # where seats hold 2 people together
            couple_to_location[person // 2].append(i // 2)

        print(couple_to_location)
        adjacency = [[] for _ in range(n)]              # map seat index to the seat indices of the partners of the
        for a, b in couple_to_location:                 # 2 people at that seat index
            adjacency[a].append(b)
            adjacency[b].append(a)

        print(adjacency)
        swaps = n                                       # for each cycle of length x, require x - 1 swaps
                                                        # so swaps = n - number of cycles
        for start in range(n):

            if not adjacency[start]:
                continue

            swaps -= 1                                  # found a cycle
            a = start                                   # starting seat index
            b = adjacency[start].pop()                  # seat index of a partner

            while b != start:
                adjacency[b].remove(a)                  # remove link in other direction
                a, b = b, adjacency[b].pop()            # move to next seat

        return swaps
