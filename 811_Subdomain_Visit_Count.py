_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subdomain-visit-count/
# A website domain like "discuss.leetcode.com" consists of various subdomains.
# At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level,
# "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent
# domains "leetcode.com" and "com" implicitly.
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed
# by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains,
# (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

# Split each cp domain into a count and list of domains. For each list of domains, form all domains (max 3) as suffixes
# of the list. Increment counts of all domains. Return list of formatted counts and domains.
# Time - O(n), since
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = defaultdict(int)                   # map a domain to its count

        for cpdomain in cpdomains:

            count, domains = cpdomain.split(" ")    # split count from domain
            domains = domains.split(".")            # split domain to components

            for i in range(len(domains)):
                domain = ".".join(domains[i:])      # build each suffix of domains
                counts[domain] += int(count)        # increment count

        return [str(count) + " " + domain for domain, count in counts.items()]  # format result