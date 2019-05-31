_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/validate-ip-address/
# Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each
# ranging from 0 to 255, separated by dots ("."). leading zeros in IPv4 are invalid.
# IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The
# groups are separated by colons (":"). Leading zeros are optional. Upper or lower case letters are allowed.
# However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons
# (::) to pursue simplicity.
# You may assume there is no extra space or special characters in the input string.

# Split by "." to check if IPv4. All group members must be integers >= 0 and <= 255. Split by ":" to check IPv6.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ip_list = IP.split(".")
        if len(ip_list) == 4:
            for group in ip_list:
                n = int(group)
                if n < 0 or n > 255 or len(str(n)) != len(group):   # len checks for leading zeros or minus zero
                    return "Neither"
            return "IPv4"

        ip_list = IP.split(":")
        if len(ip_list) != 8:
            return "Neither"

        for group in ip_list:
            n = int(group, 16)
            if n < 0 or n > int("FFFF", 16) or len(group) > 4 or group[0] == "-":   # eliminate "00000" and "-0"
                return "Neither"

        return "IPv6"