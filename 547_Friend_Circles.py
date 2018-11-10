_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/friend-circles/
# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C,
# then A is an indirect friend of C.
# We define a friend circle is a group of students who are direct or indirect friends.
# Given a N*N matrix M representing the friend relationship between students in the class, if M[i][j] = 1, then the
# ith and jth students are direct friends with each other, otherwise not.
# You have to output the total number of friend circles among all the students.

# Union find structure. Initially each friend is in their own group. Iterate over the matrix, only using the lower
# triangle because of the symmetry. For each friend relationship, union the groups by setting the group exemplar (an
# arbitrary member of the gorup) of one friend to the group exemplar of the other.
# Result is the final number of unique group exemplars.
# Alternatively, dfs for each friend marking already explored friends.
# Time - O(n**2 log* n)
# Space - O(n)

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        group = [i for i in range(n)]       # map from firend index to group exemplar

        def get_group(x):                   # get the group exemplar for x
            while group[x] != x:
                group[x] = group[group[x]]  # collapse parent to grandparent
                x = group[x]
            return x

        for i in range(1, n):
            for j in range(i):              # iterate over lower triangle of M
                if M[i][j] == 1:
                    group[get_group(i)] = get_group(j)  # set exemplar of i's group to exemplar of j's group

        return len(set(get_group(i) for i in range(n)))

class Solution2(object):
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