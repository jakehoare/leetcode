_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/freedom-trail/
# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom
# Trail Ring", and use the dial to spell a specific keyword in order to open the door.
# Given a string ring, which represents the code engraved on the outer ring and another string key, which represents
# the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters
# in the keyword.
# Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in
# the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key
# aligned at 12:00 direction and then by pressing the center button.
# At the stage of rotating the ring to spell the key character key[i]:
# You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the
# rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to
# the character key[i].
# If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which
# also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage),
# otherwise, you've finished all the spelling.

# For each char of key, for all indices in ring of this char, calculate the min distance to reach that index from
# every index of previous char. Store min distances to previous char in dictionary.
# Time - O(k * r**2) where k is length of k and r is length of ring
# Space - O(r)

from collections import defaultdict

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """

        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))

        char_to_ring = defaultdict(list)    # key is char, values is list of indices in ring of that char
        for i, c in enumerate(ring):
            char_to_ring[c].append(i)

        i_to_steps = {0: 0}  # key is index in ring, value is to min steps to reach char at that index
        for k in key:

            new_i_to_steps = {}
            new_indices = char_to_ring[k]  # indices in ring with next required character of key
            for new_i in new_indices:

                min_steps = float("inf")
                for i in i_to_steps:
                    min_steps = min(min_steps, i_to_steps[i] + dist(i, new_i))
                new_i_to_steps[new_i] = min_steps

            i_to_steps = new_i_to_steps

        return min(i_to_steps.values()) + len(key)      # add button press step for each char
