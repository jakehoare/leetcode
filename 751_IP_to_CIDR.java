/*
https://leetcode.com/problems/ip-to-cidr/
Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list
(of smallest possible length) of CIDR blocks.
A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length. For example:
"123.45.67.89/20". That prefix length "20" represents the number of common prefix bits in the specified range.

Repeatedly add to the result a CIDR block of addresses where the number of addresses is the lower of n and the bit
after the least significant set bit of IP. Bits with lower significance that are not set are contained in the block.
Increment the IP and decrement n with the size of the block.
Time - O(log n)
Space - O(log n)
*/

class Solution {

    public List<String> ipToCIDR(String ip, int n) {

        long longIP = 0;
        for (String x: ip.split("\\."))         // escape the dot
            longIP = 256 * longIP + Integer.valueOf(x);

        List<String> result = new ArrayList();

        while (n > 0) {

            int minLength = Math.min(bitLength(Long.lowestOneBit(longIP)), bitLength(n));   // 2^(minLength - 1) IPs
            int commonBits = 33 - minLength;
            result.add(longToIP(longIP) + "/" + commonBits);
            longIP += 1 << (minLength - 1);
            n -= 1 << (minLength - 1);
        }
        return result;
    }

    private String longToIP(long x) {
        return String.format("%s.%s.%s.%s",
            x >> 24, (x >> 16) % 256, (x >> 8) % 256, x % 256);
    }

    private int bitLength(long x) {
        if (x == 0)
            return 1;
        int ans = 0;
        while (x > 0) {
            x >>= 1;
            ans++;
        }
        return ans;
    }
}