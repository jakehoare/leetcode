_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-music-playlists/
# Your music player contains N different songs and she wants to listen to L (not necessarily different)
# songs during your trip.  You create a playlist so that:
# Every song is played at least once
# A song can only be played again only if K other songs have been played
# Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.

# We can extend a partial playlist by A) adding any song that has not been played before (if any), or
# B) adding a song that has been played before but is not in the K most recent songs.
# Create a mapping from the number of different songs used to the count of playlists.
# Initially there is one playlist with no songs.
# For each additional song, add playlists with every new song, If we have used more than K songs, add playlists with
# all songs not in the most recent K. Note the most recent K are all different songs.
# Time - O(LN)
# Space - O(N)

from collections import defaultdict

class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        used_count = {0: 1}     # used_count[i] is the number of playlists that have used i different songs

        for song in range(L):

            new_used_count = defaultdict(int)
            for used, count in used_count.items():

                new_used_count[used + 1] += count * (N - used)  # add any of the (N - used) unused songs
                if used > K:
                    new_used_count[used] += count * (used - K)  # add any used song not in the most recent K songs

            used_count = new_used_count

        return used_count[N] % (10 ** 9 + 7)