_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimize-max-distance-to-gas-station/
# On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1],
# where N = stations.length.
# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
# Return the smallest possible value of D.

# Create a list of distances between stations, sorted in descending order. Binary search the possible range of minimum
# max distances. Initially this range is from zero to the maximum distance between stations. Test the middle distance,
# if it is possible to put K stations with this maximum distance, test lower distances else test greater distances.
# Stop when required accuracy is achieved. Test if K stations can make the required distance by greedily using as many
# stations as required for each interval.
# Time - O(nlogn + ns) where s is the maximum number of search steps = log(r) where r = max_d / accuracy
# Space - O(n)

class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        distances = [s1 - s2 for s1, s2 in zip(stations[1:], stations)]
        distances.sort(reverse=True)

        def can_minmax_dist(d):

            remaining = K
            for dist in distances:
                if dist < d or remaining < 0:   # no more stations need to be added or no more stations left to add
                    break
                remaining -= int(dist / d)      # use stations to make the required distance

            return remaining >= 0

        max_d, min_d = distances[0], 0          # initial range for binary search

        while max_d - min_d > 10 ** -6:

            mid = (max_d + min_d) / 2.0
            if can_minmax_dist(mid):
                max_d = mid                     # try smaller distances
            else:
                min_d = mid                     # try larger distances

        return max_d

