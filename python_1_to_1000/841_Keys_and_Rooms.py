_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/keys-and-rooms/
# There are N rooms and you start in room 0. Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may
# have some keys to access the next room.
# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1]
# where N = rooms.length. A key rooms[i][j] = v opens the room with number v.
# Initially, all the rooms start locked (except for room 0).
# You can walk back and forth between rooms freely.
# Return true if and only if you can enter every room.

# Depth-first search from the first room, recursively visiting all reachable rooms and ignoring those already visited.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()

        def dfs(room):

            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)