_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/restore-ip-addresses/
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# E.g. given "25525511135", return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# For each of the 4 sections of an IP address, use 3 chars if between 100 and 255, 2 if > 10 and always use 1 char -
# provided that the remaining chars are not too few or too many to make an IP address.
# an IP address
# Time - O(1), max of 4**3 possibilities for any s
# Space - O(1)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        NB_SECTIONS = 4
        if 3 * NB_SECTIONS < len(s) < NB_SECTIONS:    # cannot make any IPs
            return []

        results = [[]]

        while NB_SECTIONS > 0:

            new_results = []

            for result in results:

                used = sum((len(section) for section in result))    # number of used characters in this partial result
                remaining = len(s) - used                           # number of remaining chars in s

                if 3 * (NB_SECTIONS - 1) >= remaining - 3 >= NB_SECTIONS - 1 and 100 <= int(s[used:used + 3]) <= 255:
                    new_results.append(result + [s[used:used + 3]])
                if 3 * (NB_SECTIONS - 1) >= remaining - 2 >= NB_SECTIONS - 1 and 10 <= int(s[used:used + 2]):
                    new_results.append(result + [s[used:used + 2]])
                if 3 * (NB_SECTIONS - 1) >= remaining - 1 >= NB_SECTIONS - 1:
                    new_results.append(result + [s[used]])

            NB_SECTIONS -= 1
            results = new_results

        return ['.'.join(result) for result in results]

