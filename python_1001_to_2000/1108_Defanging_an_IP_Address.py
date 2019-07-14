_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/defanging-an-ip-address/
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# String replace.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")
