_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ip-to-cidr/
# Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list
# (of smallest possible length) of CIDR blocks.
# A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length.
# For example: "123.45.67.89/20". Prefix length "20" represents the number of common prefix bits in the specified range.

# Convert IP to an integer and convert back when adding to results. Add to the result a block of addresses. The block
# either covers all of n or all addresses until the least significant bit of the ip address changes.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        results = []

        def num_to_ip(num):             # convert and integer to an IP address
            ip = []
            for _ in range(4):
                num, byte = divmod(num, 256)
                ip.append(str(byte))
            return ".".join(ip[::-1])

        ip_num = 0
        for byte in ip.split("."):      # convert the IP address to an integer
            ip_num = ip_num * 256 + int(byte)

        while n > 0:
            mask = 33 - min((ip_num & -ip_num).bit_length(), n.bit_length())

            results.append(num_to_ip(ip_num) + "/" + str(mask))
            ip_num += 1 << (32 - mask)
            n -= 1 << (32 - mask)

        return results