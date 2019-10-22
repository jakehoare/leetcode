_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs
# to and it's equal to -1 if the i-th item belongs to no group.
# The items and the groups are zero indexed.
# A group can have no item belonging to it.
# Return a sorted list of the items such that:
#  The items that belong to the same group are next to each other in the sorted list.
#  There are some relations between these items where beforeItems[i] is a list containing all the items that
#   should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no solution.

# Topologically sort the items in each group and topologically sort the groups.
# Topologically sort by repeatedly adding items with nothing before to the result. Then reducing the count of items
# before any items the must go after the added item, and adding it to the set of items with nothing before if the
# count is zero.
# Time - O(m + n) for m beforeItems and n items
# Space - O(m + n)

from collections import defaultdict

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """

        def top_sort(map_to_after, before_count):
            no_before = {i for i, count in before_count.items() if count == 0}  # items with nothing before
            result = []
            while no_before:
                i = no_before.pop()
                result.append(i)
                for after in map_to_after[i]:
                    before_count[after] -= 1
                    if before_count[after] == 0:
                        no_before.add(after)

            return result if len(result) == len(before_count) else []

        for i in range(n):
            if group[i] == -1:  # make a new group for this item only
                group[i] = m
                m += 1

        group_items = defaultdict(set)
        for item, gp in enumerate(group):
            group_items[gp].add(item)

        between_groups_after = defaultdict(set)             # group to set of groups before group
        groups_before_count = {gp: 0 for gp in range(m)}    # group to count of groups before
        ordered_groups = {}                                 # map group to list of sorted items

        for gp, items in group_items.items():
            within_group_after = defaultdict(set)               # item to set of items after item
            items_before_count = {item: 0 for item in items}    # item to count of items before

            for item in items:
                for before_item in beforeItems[item]:
                    if before_item in items:
                        within_group_after[before_item].add(item)
                        items_before_count[item] += 1
                    else:
                        if group[item] not in between_groups_after[group[before_item]]: # do not double count
                            groups_before_count[group[item]] += 1
                            between_groups_after[group[before_item]].add(group[item])

            ordered_items = top_sort(within_group_after, items_before_count)
            if not ordered_items:
                return []
            ordered_groups[gp] = ordered_items

        group_ordering = top_sort(between_groups_after, groups_before_count)
        if not group_ordering:
            return []

        result = []
        for gp in group_ordering:
            if gp in ordered_groups:    # ignore group with no items
                result += ordered_groups[gp]
        return result
