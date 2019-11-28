_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/video-stitching/
# You are given a series of video clips from a sporting event that lasted T seconds.
# These video clips can be overlapping with each other and have varied lengths.
# Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].
# We can cut these clips into segments freely:
# for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
# Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire
# sporting event ([0, T]). If the task is impossible, return -1.

# Sort the clips in ascending start order, with ties broken by ascending end order.
# Maintain the two greatest ends of the clips used (not necessarily the ends of the last 2 used clips).
# Iterate over the clips, breaking if there is a gap between the start of the clip and the previous end or we have
# reached the required length.
# If the start is greater than the prev_stitch_end then we must add another clip (otherwise we can replace the
# previous clip).
# Note that if end < stitch_end we may still increment the count and set prev_stitch_end = stitch_end and the clip
# will later be replaced.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        prev_stitch_end, stitch_end = -1, 0     # two greatest ends of used clips
        result = 0                              # count of used clips

        for start, end in sorted(clips):
            if start > stitch_end or stitch_end >= T:
                break

            if start > prev_stitch_end:
                result += 1
                prev_stitch_end = stitch_end

            stitch_end = max(stitch_end, end)

        return -1 if stitch_end < T else result
