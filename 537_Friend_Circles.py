_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/friend-circles/
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
# nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith
# and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend
# circles among all the students.

# DFS. For each person, start new circle if not seen before. Explore row, recursing and adding to sen et when new
# friend is found.
# Time - O(n**2)
# Space - O(n)
# Alternatively, union-find.

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1:
                    if j not in seen:
                        seen.add(j)
                        dfs(j)

        circles = 0
        seen = set()

        for i in range(len(M)):
            if i not in seen:
                circles += 1
                dfs(i)

        return circles



class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.parent = self

    def get_parent(self):
        node = self
        while node.parent != node:
            node.parent = node.parent.parent    # collapse
            node = node.parent
        return node

class Solution2(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circles = n = len(M)    # assume all people are separate circes
        person_to_node = {}     # map from index to Node
        for i in range(n):
            person_to_node[i] = Node(i)

        for i in range(n - 1):  # search above diagonal since M is symmetrical
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    i_node, j_node = person_to_node[i], person_to_node[j]
                    i_parent = i_node.get_parent()
                    j_parent = j_node.get_parent()
                    if i_parent != j_parent:
                        i_parent.parent = j_parent  # link trees
                        circles -= 1                # reduce number of independent circles

        return circles